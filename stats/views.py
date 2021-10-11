import datetime
from itertools import islice
from random import shuffle

from chartjs.colors import next_color, COLORS
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import MontagePaid, get_all_team, Team
from .charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict


@login_required()
def stats(request):
    return render(request, 'statistics.html')


@login_required()
def get_filter_options(request):
    grouped_purchases = MontagePaid.objects.annotate(year=ExtractYear('date')).values('year').order_by(
        '-year').distinct()
    options = [purchase['year'] for purchase in grouped_purchases]
    name_team = Team.objects.all()
    teams = [team for team in name_team]
    return JsonResponse({
        'options': options,
        'teams': teams,
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
        'title': f'Zarobek w {year}',
        'data': {
            'labels': list(sales_dict.keys()),
            'datasets': [{
                'label': 'Zarobek (PLN)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(sales_dict.values()),
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


class ColorsView(TemplateView):
    template_name = "colors.html"

    def get_context_data(self, **kwargs):
        data = super(ColorsView, self).get_context_data(**kwargs)
        data["colors"] = islice(next_color(), 0, 50)
        return data


class BarChartJSONView(BaseLineChartView):
    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)

    def get_labels(self):
        # print(months)
        return months

    def get_providers(self):
        teams = Team.objects.all()
        team = [team.team for team in teams]
        return team

    def get_data(self):
        teams = Team.objects.all()
        x = []
        # team = [team.salary() for team in teams]
        year = datetime.datetime.now()
        for team in teams:
            print()
            x.extend(list(team.salary()))
        print(x)
        return x


class BarChartCountJSONView(BaseLineChartView):
    def get_colors(self):
        """Return a new shuffle list of color so we change the color
        each time."""
        colors = COLORS[:]
        shuffle(colors)
        return next_color(colors)

    def get_labels(self):
        # print(months)
        return months

    def get_providers(self):
        teams = Team.objects.all()
        team = [team.team for team in teams]
        return team

    def get_data(self):
        teams = Team.objects.all()
        x = []
        # team = [team.salary() for team in teams]
        year = datetime.datetime.now()
        for team in teams:
            print()
            x.extend(list(team.count_montage()))
        print(x)
        return x


colors = ColorsView.as_view()
bar_chart = TemplateView.as_view(template_name='statistics.html')
count_bar_chart = TemplateView.as_view(template_name='statistics.html')
count_bar_chart_json = BarChartCountJSONView.as_view()
bar_chart_json = BarChartJSONView.as_view()
