from django.shortcuts import render, redirect
from .forms import cajaKpiForm,tradeKpiForm,stockKpiForm,expertasKpiForm
from .models import cajaKpi,tradeKpi,stockKpi,expertasKpi
from datetime import date,timedelta
from django.template.loader import render_to_string
from django.db.models import Count 
from django.http import JsonResponse



def kpiCaja(request):
    if request.method == 'POST':
        form = cajaKpiForm(request.POST)
        if form.is_valid():
            form.save()
            form = cajaKpiForm()  # Re-inicializar el formulario para que se muestre vacío
    else:
        form = cajaKpiForm()
    
    # Obtener datos del día actual
    hoy = date.today()
    datos_caja = cajaKpi.objects.filter(fecha=hoy)
    
    # Valor por tarea
    valor_por_tarea = 14.2857143
    
    # Calcular el porcentaje de cumplimiento por farmacia
    farmacias = cajaKpi.FARMACIA_CHOICES
    porcentaje_por_farmacia = {}
    for farmacia, _ in farmacias:
        tareas_farmacia = [entry for entry in datos_caja if entry.farmacia == farmacia]
        total_tareas_farmacia = len(tareas_farmacia)
        porcentaje_por_farmacia[farmacia] = min(total_tareas_farmacia * valor_por_tarea, 100)
    
    # Calcular el porcentaje total de cumplimiento de tareas
    total_tareas = len(datos_caja)
    total_tareas_completadas = sum(porcentaje_por_farmacia.values()) / valor_por_tarea
    porcentaje_total_cumplimiento = min(total_tareas_completadas * valor_por_tarea / len(farmacias), 100) if farmacias else 0

    # Redondear los porcentajes a números enteros
    porcentaje_total_cumplimiento = int(porcentaje_total_cumplimiento)
    porcentaje_por_farmacia = {farmacia: int(porcentaje) for farmacia, porcentaje in porcentaje_por_farmacia.items()}

    context = {
        'form': form,
        'datos_caja': datos_caja,
        'porcentaje_total_cumplimiento': porcentaje_total_cumplimiento,
        'porcentaje_por_farmacia': porcentaje_por_farmacia
    }
    return render(request, 'index.html', context)


def kpiStock(request):
    if request.method == 'POST':
        form = stockKpiForm(request.POST)
        if form.is_valid():
            form.save()
            form = stockKpiForm()  # Re-inicializar el formulario para que se muestre vacío
    else:
        form = stockKpiForm()
    
    # Obtener datos del día actual
    hoy = date.today()
    datos_stock = stockKpi.objects.filter(fecha=hoy)
    
    # Valor por tarea
    valor_por_tarea = 12.5
    
    # Calcular el porcentaje de cumplimiento por farmacia
    farmacias = stockKpi.FARMACIA_CHOICES
    porcentaje_por_farmacia = {}
    for farmacia, _ in farmacias:
        tareas_farmacia = [entry for entry in datos_stock if entry.farmacia == farmacia]
        total_tareas_farmacia = len(tareas_farmacia)
        porcentaje_por_farmacia[farmacia] = min(total_tareas_farmacia * valor_por_tarea, 100)
    
    # Calcular el porcentaje total de cumplimiento de tareas
    total_tareas = len(datos_stock)
    total_tareas_completadas = sum(porcentaje_por_farmacia.values()) / valor_por_tarea
    porcentaje_total_cumplimiento = min(total_tareas_completadas * valor_por_tarea / len(farmacias), 100) if farmacias else 0

    # Redondear los porcentajes a números enteros
    porcentaje_total_cumplimiento = int(porcentaje_total_cumplimiento)
    porcentaje_por_farmacia = {farmacia: int(porcentaje) for farmacia, porcentaje in porcentaje_por_farmacia.items()}

    context = {
        'form': form,
        'datos_stock': datos_stock,
        'porcentaje_total_cumplimiento': porcentaje_total_cumplimiento,
        'porcentaje_por_farmacia': porcentaje_por_farmacia
    }
    return render(request, 'kpiStock.html', context)


def kpiTrade(request):
    if request.method == 'POST':
        form = tradeKpiForm(request.POST)
        if form.is_valid():
            form.save()
            form = tradeKpiForm()  # Re-inicializar el formulario para que se muestre vacío
    else:
        form = tradeKpiForm()
    
    # Obtener datos del día actual
    hoy = date.today()
    datos_trade = tradeKpi.objects.filter(fecha=hoy)
    
    # Valor por tarea
    valor_por_tarea = 20
    
    # Calcular el porcentaje de cumplimiento por farmacia
    farmacias = tradeKpi.FARMACIA_CHOICES
    porcentaje_por_farmacia = {}
    for farmacia, _ in farmacias:
        tareas_farmacia = [entry for entry in datos_trade if entry.farmacia == farmacia]
        total_tareas_farmacia = len(tareas_farmacia)
        porcentaje_por_farmacia[farmacia] = min(total_tareas_farmacia * valor_por_tarea, 100)
    
    # Calcular el porcentaje total de cumplimiento de tareas
    total_tareas = len(datos_trade)
    total_tareas_completadas = sum(porcentaje_por_farmacia.values()) / valor_por_tarea
    porcentaje_total_cumplimiento = min(total_tareas_completadas * valor_por_tarea / len(farmacias), 100) if farmacias else 0

    # Redondear los porcentajes a números enteros
    porcentaje_total_cumplimiento = int(porcentaje_total_cumplimiento)
    porcentaje_por_farmacia = {farmacia: int(porcentaje) for farmacia, porcentaje in porcentaje_por_farmacia.items()}

    context = {
        'form': form,
        'datos_trade': datos_trade,
        'porcentaje_total_cumplimiento': porcentaje_total_cumplimiento,
        'porcentaje_por_farmacia': porcentaje_por_farmacia
    }
    return render(request, 'kpitrade.html', context)


def kpiExpertas(request):
    if request.method == 'POST':
        form = expertasKpiForm(request.POST)
        if form.is_valid():
            form.save()
            form = expertasKpiForm()  # Re-inicializar el formulario para que se muestre vacío
    else:
        form = expertasKpiForm()
    
    # Obtener datos del día actual
    hoy = date.today()
    datos_expertas = expertasKpi.objects.filter(fecha=hoy)
    
    # Valor por tarea
    valor_por_tarea = 25
    
    # Calcular el porcentaje de cumplimiento por farmacia
    farmacias = expertasKpi.FARMACIA_CHOICES
    porcentaje_por_farmacia = {}
    for farmacia, _ in farmacias:
        tareas_farmacia = [entry for entry in datos_expertas if entry.farmacia == farmacia]
        total_tareas_farmacia = len(tareas_farmacia)
        porcentaje_por_farmacia[farmacia] = min(total_tareas_farmacia * valor_por_tarea, 100)
    
    # Calcular el porcentaje total de cumplimiento de tareas
    total_tareas = len(datos_expertas)
    total_tareas_completadas = sum(porcentaje_por_farmacia.values()) / valor_por_tarea
    porcentaje_total_cumplimiento = min(total_tareas_completadas * valor_por_tarea / len(farmacias), 100) if farmacias else 0

    # Redondear los porcentajes a números enteros
    porcentaje_total_cumplimiento = int(porcentaje_total_cumplimiento)
    porcentaje_por_farmacia = {farmacia: int(porcentaje) for farmacia, porcentaje in porcentaje_por_farmacia.items()}

    context = {
        'form': form,
        'datos_expertas': datos_expertas,
        'porcentaje_total_cumplimiento': porcentaje_total_cumplimiento,
        'porcentaje_por_farmacia': porcentaje_por_farmacia
    }
    return render(request, 'kpiExpertas.html', context)


def kpiCoord(request):
    hoy = date.today()
    selected_farmacia = request.GET.get('farmacia', 'all')

    # Datos de cada sector filtrados por fecha y farmacia
    if selected_farmacia == 'all':
        datos_caja = cajaKpi.objects.filter(fecha=hoy)
        datos_expertas = expertasKpi.objects.filter(fecha=hoy)
        datos_stock = stockKpi.objects.filter(fecha=hoy)
        datos_trade = tradeKpi.objects.filter(fecha=hoy)
    else:
        datos_caja = cajaKpi.objects.filter(farmacia=selected_farmacia, fecha=hoy)
        datos_expertas = expertasKpi.objects.filter(farmacia=selected_farmacia, fecha=hoy)
        datos_stock = stockKpi.objects.filter(farmacia=selected_farmacia, fecha=hoy)
        datos_trade = tradeKpi.objects.filter(farmacia=selected_farmacia, fecha=hoy)

    # Calcular el porcentaje de cumplimiento
    def calcular_porcentajes(datos, total_tareas):
        # Usar un conjunto para evitar contar tareas duplicadas
        tareas_unicas = set([entry.tarea for entry in datos if entry.gestionado == 'Si'])
        total_tareas_completadas = len(tareas_unicas)
        porcentaje = (total_tareas_completadas / total_tareas) * 100
        return min(porcentaje, 100), total_tareas_completadas

    # Recuento de tareas completadas
    def contar_tareas_completadas(datos):
        return sum(1 for entry in datos if entry.gestionado == 'Si')

    # Cálculo de porcentajes y tareas completadas
    porcentaje_caja, tareas_completadas_caja = calcular_porcentajes(datos_caja, 161)
    porcentaje_expertas, tareas_completadas_expertas = calcular_porcentajes(datos_expertas, 92)
    porcentaje_stock, tareas_completadas_stock = calcular_porcentajes(datos_stock, 184)
    porcentaje_trade, tareas_completadas_trade = calcular_porcentajes(datos_trade, 115)

    # Recuento correcto de tareas completadas
    tareas_completadas_caja = contar_tareas_completadas(datos_caja)
    tareas_completadas_expertas = contar_tareas_completadas(datos_expertas)
    tareas_completadas_stock = contar_tareas_completadas(datos_stock)
    tareas_completadas_trade = contar_tareas_completadas(datos_trade)

    # Datos para gráficos de barra por sector
    grafico_datos_caja = cajaKpi.objects.filter(fecha=hoy).values('farmacia').annotate(total=Count('tarea'))
    grafico_datos_expertas = expertasKpi.objects.filter(fecha=hoy).values('farmacia').annotate(total=Count('tarea'))
    grafico_datos_stock = stockKpi.objects.filter(fecha=hoy).values('farmacia').annotate(total=Count('tarea'))
    grafico_datos_trade = tradeKpi.objects.filter(fecha=hoy).values('farmacia').annotate(total=Count('tarea'))

    farmacias = cajaKpi.FARMACIA_CHOICES

    context = {
        'datos_caja': list(datos_caja.values()),
        'datos_expertas': list(datos_expertas.values()),
        'datos_stock': list(datos_stock.values()),
        'datos_trade': list(datos_trade.values()),
        'porcentaje_caja': int(porcentaje_caja),
        'porcentaje_expertas': int(porcentaje_expertas),
        'porcentaje_stock': int(porcentaje_stock),
        'porcentaje_trade': int(porcentaje_trade),
        'tareas_completadas_caja': tareas_completadas_caja,
        'tareas_completadas_expertas': tareas_completadas_expertas,
        'tareas_completadas_stock': tareas_completadas_stock,
        'tareas_completadas_trade': tareas_completadas_trade,
        'farmacias': farmacias,
        'selected_farmacia': selected_farmacia,
        'total_tareas_caja': 161,
        'total_tareas_expertas': 92,
        'total_tareas_stock': 184,
        'total_tareas_trade': 115,
        'grafico_datos_caja': list(grafico_datos_caja),
        'grafico_datos_expertas': list(grafico_datos_expertas),
        'grafico_datos_stock': list(grafico_datos_stock),
        'grafico_datos_trade': list(grafico_datos_trade),
    }
    return render(request, 'kpiCoord.html', context)

def datos_sector(request, sector):
    hoy = date.today()
    hace_tres_dias = hoy - timedelta(days=3)
    
    if sector == 'caja':
        datos = list(cajaKpi.objects.filter(fecha__gte=hace_tres_dias).values())
    elif sector == 'expertas':
        datos = list(expertasKpi.objects.filter(fecha__gte=hace_tres_dias).values())
    elif sector == 'stock':
        datos = list(stockKpi.objects.filter(fecha__gte=hace_tres_dias).values())
    elif sector == 'trade':
        datos = list(tradeKpi.objects.filter(fecha__gte=hace_tres_dias).values())
    else:
        datos = []

    return JsonResponse(datos, safe=False)