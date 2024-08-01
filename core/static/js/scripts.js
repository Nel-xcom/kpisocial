document.addEventListener('DOMContentLoaded', function() {
    const resumenGeneralBtn = document.getElementById('resumen-general-btn');
    const detallePorFarmaciaBtn = document.getElementById('detalle-por-farmacia-btn');
    const resumenGeneralSection = document.getElementById('resumen-general');
    const detallePorFarmaciaSection = document.getElementById('detalle-por-farmacia');

    resumenGeneralBtn.addEventListener('click', function() {
        resumenGeneralSection.style.display = 'block';
        detallePorFarmaciaSection.style.display = 'none';
    });

    detallePorFarmaciaBtn.addEventListener('click', function() {
        resumenGeneralSection.style.display = 'none';
        detallePorFarmaciaSection.style.display = 'block';
    });

    const botonesSector = document.querySelectorAll('.botones-sector button');
    const filtrosContainer = document.getElementById('filtros-container');
    const datosContainer = document.getElementById('datos-container');

    botonesSector.forEach(button => {
        button.addEventListener('click', function() {
            const sector = this.id.replace('-btn', '');
            cargarFiltrosYDatos(sector);
        });
    });

    function cargarFiltrosYDatos(sector) {
        fetch(`/api/datos/${sector}`)
            .then(response => response.json())
            .then(data => {
                filtrosContainer.innerHTML = data.filtrosHTML;
                datosContainer.innerHTML = data.datosHTML;
            })
            .catch(error => console.error('Error:', error));
    }
    
    cargarGraficos(); // Función para inicializar los gráficos
});

function cargarGraficos() {
    const graficoDatosCaja = JSON.parse(document.getElementById('grafico-datos-caja').textContent);
    const graficoDatosExpertas = JSON.parse(document.getElementById('grafico-datos-expertas').textContent);
    const graficoDatosStock = JSON.parse(document.getElementById('grafico-datos-stock').textContent);
    const graficoDatosTrade = JSON.parse(document.getElementById('grafico-datos-trade').textContent);

    const graficoCaja = document.getElementById('grafico-caja').getContext('2d');
    const graficoExpertas = document.getElementById('grafico-expertas').getContext('2d');
    const graficoStock = document.getElementById('grafico-stock').getContext('2d');
    const graficoTrade = document.getElementById('grafico-trade').getContext('2d');

    crearGraficoBarras(graficoCaja, graficoDatosCaja);
    crearGraficoBarras(graficoExpertas, graficoDatosExpertas);
    crearGraficoBarras(graficoStock, graficoDatosStock);
    crearGraficoBarras(graficoTrade, graficoDatosTrade);
}

function crearGraficoBarras(ctx, datos) {
    const labels = datos.map(d => d.farmacia);
    const valores = datos.map(d => d.total);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Tareas Completadas',
                data: valores,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
