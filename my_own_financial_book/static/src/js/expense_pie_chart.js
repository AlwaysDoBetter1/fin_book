/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, onMounted, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ExpensePieChart extends Component {
    setup() {
        this.orm = useService("orm");
        this.canvasRef = useRef("pieChart");
        this.chartInstance = null;
        this.expensesData = [];

        onWillStart(async () => {
            await this.loadExpensesData();
        });

        onMounted(() => {
            this.renderChart();
        });
    }

    async loadExpensesData() {
        const bookId = this.props.record.resId;
        if (!bookId) return;

        try {
            // Читаем расходы текущей книги
            const expenses = await this.orm.searchRead(
                "fin.expense",
                [["book_id", "=", bookId]],
                ["category", "amount"]
            );

            // Группируем по категориям
            const grouped = {};
            expenses.forEach(exp => {
                const categoryName = exp.category ? exp.category[1] : "Uncategorized";
                if (!grouped[categoryName]) {
                    grouped[categoryName] = 0;
                }
                grouped[categoryName] += exp.amount || 0;
            });

            this.expensesData = Object.entries(grouped).map(([category, amount]) => ({
                category,
                amount
            }));
        } catch (error) {
            console.error("Failed to load expenses data:", error);
        }
    }

    renderChart() {
        if (!this.canvasRef.el || this.expensesData.length === 0) {
            return;
        }

        // Уничтожаем старый график если есть
        if (this.chartInstance) {
            this.chartInstance.destroy();
        }

        const ctx = this.canvasRef.el.getContext("2d");

        // Генерируем цвета для секторов
        const colors = this.generateColors(this.expensesData.length);

        // Создаем график используя Chart.js
        this.chartInstance = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: this.expensesData.map(d => d.category),
                datasets: [{
                    data: this.expensesData.map(d => d.amount),
                    backgroundColor: colors,
                    borderColor: '#fff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            font: {
                                size: 12
                            },
                            padding: 15
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${value.toFixed(2)} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    generateColors(count) {
        // Генерируем красивую палитру цветов
        const colors = [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
            '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
        ];

        // Если категорий больше чем предопределенных цветов, генерируем дополнительные
        while (colors.length < count) {
            const r = Math.floor(Math.random() * 255);
            const g = Math.floor(Math.random() * 255);
            const b = Math.floor(Math.random() * 255);
            colors.push(`rgb(${r}, ${g}, ${b})`);
        }

        return colors.slice(0, count);
    }

    willUnmount() {
        if (this.chartInstance) {
            this.chartInstance.destroy();
        }
    }
}

ExpensePieChart.template = "my_own_financial_book.ExpensePieChart";

export const expensePieChart = {
    component: ExpensePieChart,
};

registry.category("fields").add("expense_pie_chart", expensePieChart);

