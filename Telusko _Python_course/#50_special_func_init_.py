class main_store():

    def __init__(self):
        print("it's _init_...")

    def config(self):
        print("This is not the main store...")

manage = main_store

main_store.config(manage)
manage.config(main_store)

