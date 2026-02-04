class ChaiUtilis:
    @staticmethod
    def  clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water ,    milk   ,  ginger, honey "

# obj = ChaiUtilis()
# print(obj.clean_ingredients(raw))



Cleaned = ChaiUtilis.clean_ingredients(raw)
print(Cleaned)