const ctx = document.getElementById('salesChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['iPhone 14', 'iPhone SE', 'iPhone 13'],
        datasets: [{
            label: 'Sales',
            data: [120000, 80000, 95000],
            backgroundColor: '#1d1d1f'
        }]
    }
});
