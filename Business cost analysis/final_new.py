## Final GUI Project submitted by Youssef Afifi in partial fulfillment of CSIS 1300

## 4/18/2023

## Business cost beneift analysis with GUI
import tkinter as tk
from tkinter import ttk
class CostBenefitAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Startup Cost Benefit Analysis")

        self.mainframe = ttk.Frame(self.root, padding="10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.create_widgets()

    def create_widgets(self):
        self.initial_capital_investment_entry = ttk.Entry(self.mainframe)
        self.monthly_location_lease_entry = ttk.Entry(self.mainframe)
        self.monthly_location_utilities_entry = ttk.Entry(self.mainframe)
        self.num_employees_entry = ttk.Entry(self.mainframe)
        self.hourly_pay_rate_entry = ttk.Entry(self.mainframe)
        self.weekly_work_hours_entry = ttk.Entry(self.mainframe)
        self.num_products_entry = ttk.Entry(self.mainframe)

        self.products_entries = {}
        self.product_frames = []

        self.num_products_entry.bind("<FocusOut>", lambda e: self.create_product_entries())

        ttk.Label(self.mainframe, text="Enter amount of Initial Capital Investment:").grid(column=0, row=0, sticky=tk.W)
        self.initial_capital_investment_entry.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self.mainframe, text="Enter the Monthly Location Lease Costs:").grid(column=0, row=1, sticky=tk.W)
        self.monthly_location_lease_entry.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self.mainframe, text="Enter the Monthly Location Utilities Costs:").grid(column=0, row=2, sticky=tk.W)
        self.monthly_location_utilities_entry.grid(column=1, row=2, sticky=tk.W)
        
        ttk.Label(self.mainframe, text="How many Employees do you have:").grid(column=0, row=3, sticky=tk.W)
        self.num_employees_entry.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self.mainframe, text="What is their hourly pay rate:").grid(column=0, row=4, sticky=tk.W)
        self.hourly_pay_rate_entry.grid(column=1, row=4, sticky=tk.W)

        ttk.Label(self.mainframe, text="How many hours a week do they work:").grid(column=0, row=5, sticky=tk.W)
        self.weekly_work_hours_entry.grid(column=1, row=5, sticky=tk.W)

        ttk.Label(self.mainframe, text="How many products do you sell:").grid(column=0, row=6, sticky=tk.W)
        self.num_products_entry.grid(column=1, row=6, sticky=tk.W)

        self.result_text = tk.StringVar()
        self.result_label = ttk.Label(self.mainframe, textvariable=self.result_text)
        self.result_label.grid(column=0, row=20, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.calculate_button = ttk.Button(self.mainframe, text="Calculate", command=self.calculate)
        self.calculate_button.grid(column=0, row=21, columnspan=2)

    def create_product_entries(self):
        num_products = int(self.num_products_entry.get())

        for i in range(len(self.product_frames), num_products):
            product_frame = ttk.Frame(self.mainframe, padding="10")
            product_frame.grid(column=0, row=9 + i, sticky=(tk.W, tk.E, tk.N, tk.S))
            self.product_frames.append(product_frame)
            product_name_entry =ttk.Entry(product_frame)
            unit_cost_entry = ttk.Entry(product_frame)
            unit_sales_price_entry = ttk.Entry(product_frame)
            units_sold_entry = ttk.Entry(product_frame)
            self.products_entries[i] = {
                'name': product_name_entry,
                'unit_cost': unit_cost_entry,
                'unit_sales_price': unit_sales_price_entry,
                'units_sold': units_sold_entry
            }
            ttk.Label(product_frame, text=f"Product {i + 1}:").grid(column=0, row=0, sticky=tk.W)
            ttk.Label(product_frame, text="Product Name:").grid(column=1, row=0, sticky=tk.W)
            product_name_entry.grid(column=2, row=0, sticky=tk.W)
            ttk.Label(product_frame, text="Unit Cost:").grid(column=1, row=1, sticky=tk.W)
            unit_cost_entry.grid(column=2, row=1, sticky=tk.W)
            ttk.Label(product_frame, text="Unit Sales Price:").grid(column=1, row=2, sticky=tk.W)
            unit_sales_price_entry.grid(column=2, row=2, sticky=tk.W)
            ttk.Label(product_frame, text="Units Sold a Month:").grid(column=1, row=3, sticky=tk.W)
            units_sold_entry.grid(column=2, row=3, sticky=tk.W)

    def calculate(self):
            capital_investment = float(self.initial_capital_investment_entry.get())
            location_costs = float(self.monthly_location_lease_entry.get()) + float(self.monthly_location_utilities_entry.get())
            num_employees = int(self.num_employees_entry.get())
            hourly_pay_rate = float(self.hourly_pay_rate_entry.get())
            weekly_work_hours = float(self.weekly_work_hours_entry.get())
            num_products = int(self.num_products_entry.get())

            employee_costs = num_employees * hourly_pay_rate * weekly_work_hours * 4
            monthly_operational_expenditures = location_costs + employee_costs
            emp_cost =num_employees*hourly_pay_rate*weekly_work_hours*52/12
            total_sales = 0

            #for i in range(num_products):
            #    product_name = self.products_entries[i]['name'].get()
            #    unit_cost = float(self.products_entries[i]['unit_cost'].get())
            #    unit_sales_price = float(self.products_entries[i]['unit_sales_price'].get())
            #    units_sold = float(self.products_entries[i]['units_sold'].get())
            #    proj_sales =units_sold*(unit_sales_price-unit_cost)
            #    product_sales = (unit_sales_price - unit_cost) * units_sold
            #    total_sales += product_sales
            #    total_month_sale = units_sold *(unit_sales_price-unit_cost)
            #for i in range(num_products):
             #   result=f" The projected Monthly Unit Sales for {product_name[i]} will generate ${total_month_sale[i]} in 3 months"   
            product_output_text = []

            for i in range(num_products):
                product_name = self.products_entries[i]['name'].get()
                unit_cost = float(self.products_entries[i]['unit_cost'].get())
                unit_sales_price = float(self.products_entries[i]['unit_sales_price'].get())
                units_sold = float(self.products_entries[i]['units_sold'].get())
                product_sales = (unit_sales_price - unit_cost) * units_sold
                total_sales += product_sales

                product_output_text.append(
                    f"{i + 1}: {product_name}\n\n"
                    f"Unit Cost: $ {unit_cost:.2f}\n\n"
                    f"Unit Sales Price: $ {unit_sales_price:.2f}\n\n"
                    f"Units Sold a Month: {units_sold}\n\n"
                    f"The projected Monthly {product_name} Sales Volume = $ {product_sales:,.2f}\n"
                    f"\nThe total Monthly Unit Sales Volume = $ {total_sales:,.2f}\n"
                )

            product_output = "\n".join(product_output_text)
            


            months_covered = round(capital_investment / monthly_operational_expenditures)
            tempmonth=3
            sales_in_months = total_sales * tempmonth
            profit_loss = tempmonth - capital_investment
            total_incoming = total_sales * tempmonth
            total_outgoing = monthly_operational_expenditures * tempmonth
            net_income=total_incoming-total_outgoing
            result = f"This business venture will generate ${net_income:,.2f} in {'LOSS' if profit_loss < 0 else 'PROFIT'} in {months_covered:.2f} months\n"
            result += f"The projected Monthly Location Expenditures = ${location_costs:,.2f}\n"
            result+=f"The projected Monthly Employee Expenditures = ${emp_cost:,.2f}\n"
            result+=f"The Monthly Operational Expenditures = ${emp_cost+location_costs:,.2f}\n"
            result+=f"The Capital Investment of ${capital_investment:,.2f} will cover 3 months of Operational Expenditures\n"
            #result+=f"The projected Monthly {product_name} sales volume = ${proj_sales:,.2f}\n"
            #result+=f"The projected Monthly {product_name} sales volume = ${proj_sales:,.2f}\n"
            result+=f"The projected ${product_output} "
            self.result_text.set(result)
    ## v1.0 (old)def calculate(self):
     #   capital_investment = float(self.initial_capital_investment_entry.get())
     #   location_costs = float(self.monthly_location_lease_entry.get()) + float(self.monthly_location_utilities_entry.get())
     #   num_employees = int(self.num_employees_entry.get())
     #   hourly_pay_rate = float(self.hourly_pay_rate_entry.get())
     #   weekly_work_hours = float(self.weekly_work_hours_entry.get())
     #   num_products = int(self.num_products_entry.get())
#
     #   employee_costs = num_employees * hourly_pay_rate * weekly_work_hours * 4
     #   monthly_operational_expenditures = location_costs + employee_costs
     #   total_sales = 0
     #   
#
     #   for i in range(num_products):
     #       product_name = self.products_entries[i]['name'].get()
     #       unit_cost = float(self.products_entries[i]['unit_cost'].get())
     #       unit_sales_price = float(self.products_entries[i]['unit_sales_price'].get())
     #       units_sold = float(self.products_entries[i]['units_sold'].get())
#
     #       product_sales = (unit_sales_price - unit_cost) * units_sold
     #       total_sales += product_sales
#
     #   months_covered = capital_investment / monthly_operational_expenditures
     #   sales_in_months = total_sales * months_covered
     #   profit_loss = sales_in_months - capital_investment
#
     #   self.result_text.set(f"This business venture will generate ${profit_loss:,.2f} in {'LOSS' if profit_loss < 0 else 'PROFIT'} in {months_covered:.2f} months")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CostBenefitAnalysisApp(root)
    root.mainloop()
