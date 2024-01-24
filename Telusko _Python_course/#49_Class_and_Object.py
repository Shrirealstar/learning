class main_store():
    def config(self):
        print("This is not the main store...")

manage = main_store


main_store.config(manage)# Example 1
manage.config(main_store)# Example 2
