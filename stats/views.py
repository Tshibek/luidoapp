from django.contrib.auth.decorators import login_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from core.models import MontagePaid, get_all_team
from .charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict


@login_required()
def get_filter_options(request):
    grouped_purchases = MontagePaid.objects.annotate(year=ExtractYear('date')).values('year').order_by(
        '-year').distinct()
    options = [purchase['year'] for purchase in grouped_purchases]

    return JsonResponse({
        'options': options,
    })


@login_required()
def get_sales_chart(request, year, team):
    purchases = MontagePaid.objects.filter(date__year=year, montage__team__team=team)
    grouped_purchases = purchases.annotate(month=ExtractMonth('date')) \
        .values('month').annotate(average=Sum('paid')).values('month', 'average').order_by(
        'month')

    sales_dict = get_year_dict()

    for group in grouped_purchases:
        sales_dict[months[group['month'] - 1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Zarobek in {year}',
        'data': {
            'labels': list(sales_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(sales_dict.values()),
            }]
        },
    })

    @login_required()
    def payment_success_chart(request, year):
        purchases = MontagePaid.objects.filter(date__year=year)

        return JsonResponse({
            'title': f'Payment success rate in {year}',
            'data': {
                'labels': ['Successful', 'Unsuccessful'],
                'datasets': [{
                    'label': 'Amount ($)',
                    'backgroundColor': [colorSuccess, colorDanger],
                    'borderColor': [colorSuccess, colorDanger],
                    'data': [
                        purchases.count(),

                    ],
                }]
            },
        })

    # @login_required()
    # def payment_method_chart(request, year):
    #     purchases = MontagePaid.objects.filter(date__year=year)
    #     grouped_purchases = purchases.values('days').annotate(count=Count('id')) \
    #         .values('days', 'count').order_by('days')
    #
    #     payment_method_dict = dict()
    #
    #     for payment_method in Purchase.PAYMENT_METHODS:
    #         payment_method_dict[payment_method[1]] = 0
    #
    #     for group in grouped_purchases:
    #         payment_method_dict[dict(Purchase.PAYMENT_METHODS)[group['payment_method']]] = group['count']
    #
    #     return JsonResponse({
    #         'title': f'Payment method rate in {year}',
    #         'data': {
    #             'labels': list(payment_method_dict.keys()),
    #             'datasets': [{
    #                 'label': 'Amount ($)',
    #                 'backgroundColor': generate_color_palette(len(payment_method_dict)),
    #                 'borderColor': generate_color_palette(len(payment_method_dict)),
    #                 'data': list(payment_method_dict.values()),
    #             }]
    #         },
    #     })
