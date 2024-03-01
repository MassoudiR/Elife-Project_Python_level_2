from CTkMessagebox import CTkMessagebox
import customtkinter
import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from CTkTable import *
from CTkListbox import *
import datetime




class AddProductWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ajouter un Produit")
        self.geometry("800x800")

        self.sku_label = customtkinter.CTkLabel(self, text="SKU:")
        self.sku_label.grid(row=0, column=0, sticky="nsew", pady=10)
        self.sku_entry = customtkinter.CTkEntry(self, width=200)
        self.sku_entry.grid(row=1, column=0, sticky="nsew", pady=10)

        self.name_label = customtkinter.CTkLabel(self, text="Nom:")
        self.name_label.grid(row=2, column=0, sticky="nsew", pady=10)
        self.name_entry = customtkinter.CTkEntry(self, width=200)
        self.name_entry.grid(row=3, column=0, sticky="nsew", pady=10)

        self.price_label = customtkinter.CTkLabel(self, text="Prix:")
        self.price_label.grid(row=4, column=0, sticky="nsew", pady=10)
        self.price_entry = customtkinter.CTkEntry(self, width=200)
        self.price_entry.grid(row=5, column=0, sticky="nsew", pady=10)

        self.quantity_label = customtkinter.CTkLabel(self, text="Quantité:")
        self.quantity_label.grid(row=6, column=0, sticky="nsew", pady=10)
        self.quantity_entry = customtkinter.CTkEntry(self, width=200)
        self.quantity_entry.grid(row=7, column=0, sticky="nsew", pady=10)
        
        self.expiry_date_label = customtkinter.CTkLabel(self, text="Date d'expiration (AAAA-MM-JJ):")
        self.expiry_date_label.grid(row=9, column=0, sticky="nsew", pady=10)
        self.expiry_date_entry = customtkinter.CTkEntry(self, width=200)
        self.expiry_date_entry.grid(row=10, column=0, sticky="nsew", pady=10)

        self.category = customtkinter.CTkLabel(self, text="Categorie:")
        self.category.grid(row=11, column=0, sticky="nsew", pady=10)
        self.category_entry = customtkinter.CTkEntry(self, width=200)
        self.category_entry.grid(row=12, column=0, sticky="nsew", pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Ajouter", command=self.on_add_clicked)
        self.add_button.grid(row=13, column=0, sticky="nsew", pady=10)

        self.grid_columnconfigure(0, weight=1)
        for i in range(13):
            self.grid_rowconfigure(i, weight=1)

    def on_add_clicked(self):
        sku = self.sku_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        expiry_date = self.expiry_date_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_entry.get()

        
        product_info = f"SKU: {sku}, Name: {name}, Price: {price}, Expiry Date: {expiry_date}, Quantity: {quantity}, Category: {category}\n"

        
        with open("product.txt", "a") as file:
            file.write(product_info)

        
        self.clear_entry_fields()

    def clear_entry_fields(self):
        
        self.sku_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.expiry_date_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')
        self.category_entry.delete(0, 'end')


class UpdateProductWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Mettre à Jour un Produit")
        self.geometry("800x600")

        self.sku_label = customtkinter.CTkLabel(self, text="SKU du Produit à Mettre à Jour:")
        self.sku_label.grid(row=0, column=0, sticky="nsew", pady=10)

        sku_options = self.get_sku_options()

        try :
            self.selected_sku = customtkinter.StringVar(value=sku_options[0])
        except:
            self.selected_sku = customtkinter.StringVar(value="")

        self.sku_optionmenu = customtkinter.CTkOptionMenu(
            self, values=sku_options, variable=self.selected_sku, dynamic_resizing=False)
        self.sku_optionmenu.grid(row=1, column=0,  pady=10)

        self.new_name_label = customtkinter.CTkLabel(self, text="Nouveau Nom:")
        self.new_name_label.grid(row=2, column=0, sticky="nsew", pady=10)
        self.new_name_entry = customtkinter.CTkEntry(self, width=200)
        self.new_name_entry.grid(row=3, column=0, sticky="nsew", pady=10)

        self.new_price_label = customtkinter.CTkLabel(self, text="Nouveau Prix:")
        self.new_price_label.grid(row=4, column=0, sticky="nsew", pady=10)
        self.new_price_entry = customtkinter.CTkEntry(self, width=200)
        self.new_price_entry.grid(row=5, column=0, sticky="nsew", pady=10)

        self.new_quantity_label = customtkinter.CTkLabel(self, text="Nouvelle Quantité:")
        self.new_quantity_label.grid(row=6, column=0, sticky="nsew", pady=10)
        self.new_quantity_entry = customtkinter.CTkEntry(self, width=200)
        self.new_quantity_entry.grid(row=7, column=0, sticky="nsew", pady=10)
        
        self.new_expiry_date_label = customtkinter.CTkLabel(self, text="Nouvelle Date d'expiration (AAAA-MM-JJ):")
        self.new_expiry_date_label.grid(row=8, column=0, sticky="nsew", pady=10)
        self.new_expiry_date_entry = customtkinter.CTkEntry(self, width=200)
        self.new_expiry_date_entry.grid(row=9, column=0, sticky="nsew", pady=10)

        self.update_button = customtkinter.CTkButton(self, text="Mettre à Jour", command=self.on_update_clicked)
        self.update_button.grid(row=10, column=0, sticky="nsew", pady=10)

        self.grid_columnconfigure(0, weight=1)
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)

    def get_sku_options(self):
        with open("product.txt", "r") as file:
            lines = file.readlines()

        sku_options = []
        for line in lines:
            if line.startswith("SKU:"):
                sku = line.split(",")[0].replace("SKU: ", "")
                sku_options.append(sku)

        return sku_options

    def on_update_clicked(self):
        sku = self.selected_sku.get()
        new_name = self.new_name_entry.get()
        new_price = self.new_price_entry.get()
        new_expiry_date = self.new_expiry_date_entry.get()
        new_quantity = self.new_quantity_entry.get()

        with open("product.txt", "r") as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            if line.startswith(f"SKU: {sku}"):
                parts = line.split(", ")
                parts[1] = f"Name: {new_name}"
                parts[2] = f"Price: {new_price}"
                parts[3] = f"Expiry Date: {new_expiry_date}"
                parts[4] = f"Quantity: {new_quantity}"
                line = ", ".join(parts)
            updated_lines.append(line)

        with open("product.txt", "w") as file:
            file.writelines(updated_lines)

        self.clear_entry_fields()

    def clear_entry_fields(self):
        self.new_name_entry.delete(0, 'end')
        self.new_price_entry.delete(0, 'end')
        self.new_expiry_date_entry.delete(0, 'end')
        self.new_quantity_entry.delete(0, 'end')

class DeleteProductWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Supprimer un Produit")
        self.geometry("600x400")

        self.sku_label = customtkinter.CTkLabel(self, text="SKU du Produit à Supprimer:")
        self.sku_label.grid(row=0, column=0, sticky="nsew", pady=10)

        sku_options = self.get_sku_options()

        try :
            self.selected_sku = customtkinter.StringVar(value=sku_options[0])
        except:
            self.selected_sku = customtkinter.StringVar(value="")

        self.sku_optionmenu = customtkinter.CTkOptionMenu(
            self, values=sku_options, variable=self.selected_sku, dynamic_resizing=False)
        self.sku_optionmenu.grid(row=1, column=0)

        self.delete_button = customtkinter.CTkButton(self, text="Supprimer", command=self.on_delete_clicked)
        self.delete_button.grid(row=2, column=0, sticky="nsew", pady=10)

        self.grid_columnconfigure(0, weight=1)
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)

    def get_sku_options(self):
        with open("product.txt", "r") as file:
            lines = file.readlines()

        sku_options = []
        for line in lines:
            if line.startswith("SKU:"):
                sku = line.split(",")[0].replace("SKU: ", "")
                sku_options.append(sku)

        return sku_options

    def on_delete_clicked(self):
        sku = self.selected_sku.get()

        with open("product.txt", "r") as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            if not line.startswith(f"SKU: {sku}"):
                updated_lines.append(line)

        with open("product.txt", "w") as file:
            file.writelines(updated_lines)
        

        CTkMessagebox(icon="check",title="Success", message=f"Product with SKU {sku} has been deleted." , option_1="Ok")
        self.destroy()
        self.update()

        self.selected_sku.set(self.get_sku_options()[0])

class ShowAllProductsWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Afficher tous les Produits")
        self.geometry("1050x600")

        self.filter_frame = customtkinter.CTkFrame(self)
        self.filter_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.sku_label = customtkinter.CTkLabel(self.filter_frame, text="Rechercher par SKU:")
        self.sku_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.sku_entry = customtkinter.CTkEntry(self.filter_frame)
        self.sku_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        self.name_label = customtkinter.CTkLabel(self.filter_frame, text="Rechercher par Nom:")
        self.name_label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.name_entry = customtkinter.CTkEntry(self.filter_frame)
        self.name_entry.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        self.category_label = customtkinter.CTkLabel(self.filter_frame, text="Rechercher par Catégorie:")
        self.category_label.grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.category_combobox = customtkinter.CTkComboBox(self.filter_frame, command=self.search)
        self.category_combobox.grid(row=0, column=5, sticky="ew", padx=5, pady=5)
        self.category_combobox.set("Sélectionnez une catégorie")

        self.clear_button = customtkinter.CTkButton(self.filter_frame, text="Effacer les filtres", command=self.clear_filters)
        self.clear_button.grid(row=0, column=6, sticky="e", padx=5, pady=5)

        self.tree = ttk.Treeview(self, columns=("SKU", "Name", "Price", "Quantity", "Expiry Date", "Category"), show="headings")
        self.tree.heading("SKU", text="SKU")
        self.tree.heading("Name", text="Nom")
        self.tree.heading("Price", text="Prix")
        self.tree.heading("Quantity", text="Quantité")
        self.tree.heading("Expiry Date", text="Date d'expiration")
        self.tree.heading("Category", text="Catégorie")

        self.tree.grid(row=1, column=0, columnspan=2, sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        for column in ("SKU", "Name", "Price", "Quantity", "Expiry Date", "Category"):
            self.tree.column(column, width=100, anchor="center")
            self.tree.heading(column, text=column)

        self.populate_treeview()
        self.populate_categories()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.sku_entry.bind("<KeyRelease>", self.search)
        self.name_entry.bind("<KeyRelease>", self.search)


    def populate_treeview(self):
        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("SKU"):
                parts = line.split(", ")
                sku = parts[0].replace("SKU: ", "")
                name = parts[1].replace("Name: ", "")
                price = parts[2].replace("Price: ", "")
                quantity = parts[4].replace("Quantity: ", "")
                expiry_date = parts[3].replace("Expiry Date: ", "")
                category = parts[5].replace("Category: ", "")

                self.tree.insert("", "end", values=(sku, name, price, quantity, expiry_date, category))

    def populate_categories(self):
        categories = set()
        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            if "Category:" in line:
                category = line.split("Category:")[1].strip()
                categories.add(category)

        self.category_combobox.configure(values=list(categories))

    def search(self, event=None):
        sku_query = self.sku_entry.get()
        name_query = self.name_entry.get()
        category_query = self.category_combobox.get()

        for item in self.tree.get_children():
            self.tree.delete(item)

        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("SKU"):
                parts = line.split(", ")
                sku = parts[0].replace("SKU: ", "")
                name = parts[1].replace("Name: ", "")
                price = parts[2].replace("Price: ", "")
                quantity = parts[4].replace("Quantity: ", "")
                expiry_date = parts[3].replace("Expiry Date: ", "")
                category = parts[5].replace("Category: ", "")

                if (sku_query.lower() in sku.lower()) and (name_query.lower() in name.lower()) and (category_query == "Sélectionnez une catégorie" or (category_query + '\n') == category):
                    self.tree.insert("", "end", values=(sku, name, price, quantity, expiry_date, category))

    def clear_filters(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.sku_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.category_combobox.set("Sélectionnez une catégorie")
        self.populate_treeview()

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Supprimer", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return



class BuyProductFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        
        self.products = {}  

        self.product_prices = {}
        self.product_stock = {}

        self.sku_label = customtkinter.CTkLabel(self, text="Sélectionner le SKU du produit:")
        self.sku_label.grid(row=0, column=0, padx=10, pady=10)
        
        sku_options = self.get_sku_options()
        try :
            self.selected_sku = customtkinter.StringVar(value=sku_options[0])
        except:
            self.selected_sku = customtkinter.StringVar(value="")

        self.sku_optionmenu = customtkinter.CTkOptionMenu(
            self, values=sku_options, variable=self.selected_sku, dynamic_resizing=False, command=self.update_total)
        self.sku_optionmenu.grid(row=0, column=1, padx=10, pady=10)

        self.quantity_label = customtkinter.CTkLabel(self, text="Quantité:")
        self.quantity_label.grid(row=0, column=2, padx=10, pady=10)
        self.quantity_entry = customtkinter.CTkEntry(self)
        self.quantity_entry.grid(row=0, column=3, padx=10, pady=10)
        self.quantity_entry.insert(0, '1') 

        self.total_label = customtkinter.CTkLabel(self, text="Total:")
        self.total_label.grid(row=0, column=4, padx=10, pady=10)
        self.total_value_label = customtkinter.CTkLabel(self, text="0")
        self.total_value_label.grid(row=0, column=5, padx=10, pady=10)

        self.add_to_cart_button = customtkinter.CTkButton(
            self, text="Ajouter au panier", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=0, column=6, padx=10, pady=10)

        self.cart_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.delete_item, corner_radius=0)
        self.cart_frame.grid(row=1, column=0, columnspan=7, padx=10, pady=10, sticky="we")

        self.load_product_data()

        self.update_total()
        self.quantity_entry.bind("<KeyRelease>", self.update_total)

        self.total_purchase_label = customtkinter.CTkLabel(self, text="Total des achats: 0")
        self.total_purchase_label.grid(row=2, column=0, columnspan=7, padx=10, pady=10, sticky="we")

        self.confirm_button = customtkinter.CTkButton(
            self, text="Confirmer", command=self.confirm)
        self.confirm_button.grid(row=3, column=0, columnspan=7, padx=10, pady=10, sticky="we")

    def delete_item(self, item):
        self.cart_frame.remove_item(item)
        
        self.update_total_purchase()

    def get_sku_options(self):
        with open("product.txt", "r") as file:
            lines = file.readlines()

        sku_options = []
        for line in lines:
            if line.startswith("SKU:"):
                parts = line.split(", ")
                sku = parts[0].replace("SKU: ", "")
                stock = int(parts[4].replace("Quantity: ", ""))
                sku_options.append(sku)
                self.product_stock[sku] = stock

        return sku_options

    def load_product_data(self):
        with open("product.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("SKU:"):
                parts = line.split(", ")
                sku = parts[0].replace("SKU: ", "")
                price = float(parts[2].replace("Price: ", ""))
                self.product_prices[sku] = price
                name = parts[1].replace("Name: ", "")
                self.products[sku] = name

    def update_total(self, event=None):
        try:
            sku = self.selected_sku.get()
            if self.quantity_entry.get() == "" or self.quantity_entry.get() == " ":
                quantity = 1
            else : 
                quantity = int(self.quantity_entry.get())

            if sku in self.product_prices:
                price_per_unit = self.product_prices[sku]
                total = quantity * price_per_unit

                
                if quantity > self.product_stock[sku]:
                    CTkMessagebox(self,icon="cancel", title="Erreur", message="Quantité non disponible dans le stock", option_1="Ok")
                    self.quantity_entry.delete(0, 'end')
                    self.quantity_entry.insert(0, '1')
                    return

                self.total_value_label.configure(text=str(total))
        except ValueError as e:
            
            CTkMessagebox(self,icon="cancel", title="Erreur", message="Veuillez entrer une quantité valide", option_1="Ok")

    def add_to_cart(self):
        try:
            sku = self.selected_sku.get()
            quantity = int(self.quantity_entry.get())
            
            
            if quantity > self.product_stock[sku]:
                raise ValueError("Quantité non disponible dans le stock")

            
            product_info = f"SKU: {sku}  ({self.products[sku]}) | {self.product_prices[sku]} * {quantity}  |  Total: {self.product_prices[sku] * quantity}"
            self.cart_frame.add_item(product_info)

            
            CTkMessagebox(icon="info", title="Ajouté au panier", message=product_info, option_1="Ok")

            
            self.quantity_entry.delete(0, 'end')
            self.quantity_entry.insert(0, '1')

            
            self.update_total_purchase()
        except ValueError as e:
            
            CTkMessagebox(icon="error", title="Erreur", message=str(e), option_1="Ok")

    def update_total_purchase(self):
        
        total_purchase = sum([float(label.cget("text").split()[-1]) for label in self.cart_frame.label_list])
        
        self.total_purchase_label.configure(text=f"Total des achats: {total_purchase}")

    def confirm(self):
        try:
            
            now = datetime.datetime.now()
            current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

            
            with open("purchase_history.txt", "a") as file:
                for label in self.cart_frame.label_list:
                    item = label.cget("text").split()[1]
                    quantity = int((label.cget("text").split('|')[1]).split('*')[1])
                    price = float((label.cget("text").split('|')[2]).split()[1])
                    file.write(f"SKU: {item}, Quantity: {quantity}, Price: {price}, Date: {current_datetime}\n")
                file.write("\n")

            
            with open("product.txt", "r") as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                if line.startswith("SKU:"):
                    parts = line.split(", ")
                    sku = parts[0].replace("SKU: ", "")
                    stock = int(parts[4].replace("Quantity: ", ""))
                    for label in self.cart_frame.label_list:
                        purchased_sku = label.cget("text").split()[1]
                        purchased_quantity = int((label.cget("text").split('|')[1]).split('*')[1])
                        if purchased_sku == sku:
                            stock -= purchased_quantity
                    updated_line = f"SKU: {sku}, Name: {parts[1]}, Price: {parts[2]}, Expiry Date: {parts[3]}, Quantity: {stock}, Category: {parts[5]}"
                    updated_lines.append(updated_line)
                else:
                    updated_lines.append(line)

            with open("product.txt", "w") as file:
                file.writelines(updated_lines)

            
            self.cart_frame.destroy()

            
            self.total_purchase_label.configure(text="Total des achats: 0")

            
            self.products.clear()
            self.product_prices.clear()
            self.product_stock.clear()

            
            self.load_product_data()

            CTkMessagebox(icon="info", title="Achat Confirmé", message="Achat confirmé avec succès.", option_1="Ok")
        except Exception as e:
            CTkMessagebox(icon="error", title="Erreur", message=str(e), option_1="Ok")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion de stock")
        self.geometry("1200x750")
        self.add_window = None
        self.update_window = None
        self.delete_window = None
        self.show_window = None

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assest")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_OpenMindsP.png")), size=(190, 37))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(864, 138.6))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.addBtn = customtkinter.CTkImage(Image.open(os.path.join(image_path, "add-btn.png")), size=(364, 99))
        self.editBtn = customtkinter.CTkImage(Image.open(os.path.join(image_path, "edit-btn.png")), size=(364, 99))
        self.deleteBtn = customtkinter.CTkImage(Image.open(os.path.join(image_path, "remove-btn.png")), size=(364, 99))
        self.showBtn = customtkinter.CTkImage(Image.open(os.path.join(image_path, "show-btn.png")), size=(364, 99))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.buy_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "buy_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "buy_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="vente",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.buy_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        #self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
        #                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                              image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        #self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.addBtn, fg_color="transparent",compound="top" , command=self.open_AddProductWindow)
        self.home_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="", image=self.editBtn, fg_color="transparent",compound="top" , command=self.open_UpdateWindow)
        self.home_frame_button_2.grid(row=4, column=0, padx=20, pady=10)

        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="", image=self.deleteBtn, fg_color="transparent",compound="top" , command=self.open_DeleteWindow)
        self.home_frame_button_3.grid(row=5, column=0, padx=20, pady=10)

        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="", image=self.showBtn, fg_color="transparent",compound="top" , command=self.open_ShowWindow)
        self.home_frame_button_4.grid(row=6, column=0, padx=20, pady=10)


        
        self.second_frame = BuyProductFrame(self)
        self.second_frame.grid(row=0, column=1, sticky="nsew")


        
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")



        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        ##self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def open_AddProductWindow(self):
        if self.add_window is None or not self.add_window.winfo_exists():
            self.add_window = AddProductWindow(self)  
        else:
            self.add_window.focus() 
    
    def open_UpdateWindow(self):
        if self.update_window is None or not self.update_window.winfo_exists():
            self.update_window = UpdateProductWindow(self)  
        else:
            self.update_window.focus()
            
    def open_DeleteWindow(self):
        if self.delete_window is None or not self.delete_window.winfo_exists():
            self.delete_window = DeleteProductWindow(self)  
        else:
            self.delete_window.focus()
    
    def open_ShowWindow(self):
        if self.show_window is None or not self.show_window.winfo_exists():
            self.show_window = ShowAllProductsWindow(self)  
        else:
            self.show_window.focus()
        
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
