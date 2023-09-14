from googletrans import Translator

translator = Translator()

responses = {}

district_options = {
    "1": "ਪਟਿਆਲਾ",
    "2": "ਹੋਰ",
    "3": "ਬੋਟ ਬੰਦ ਕਰਨ ਲਈ"
}

# Define options for block selection in Patiala district
patiala_block_options = {
    "1": "ਪਟਿਆਲਾ",
    "2": "ਨਾਭਾ",
    "3": "ਰਾਜਪੁਰਾ",
    "4": "ਪੁਨਰਹੇੜੀ",
    "5": "ਸਨੌਰ",
    "6": "ਸਮਾਣਾ",
    "7": "ਘਨੌਰ",
    "8": "ਪਾਤੜਾਂ"
}

user_data = {
    "district": "",
    "village": "",
    "name": "",
    "burn_paddy_straw": "",
    "make_straw_bales": "",
    "harvest_month": ""
}

def respond_to_input(input_text):
    input_text = input_text.strip()
    
    if input_text in responses:
        return responses[input_text]
    else:
        try:
            translation = translator.translate(input_text, src='en', dest='pa')
            return translation.text
        except Exception as e:
            return "ਮੈਂ ਸਮਝ ਨਹੀਂ ਸਕਦਾ."

print("ਪਿਆਰੇ ਕਿਸਾਨ ਭਰਾਵੋ ਸਤਿ-ਸ੍ਰੀ ਅਕਾਲ ਜ਼ਿਲ੍ਹਾ ਪ੍ਰਸ਼ਾਸਨ ਪਟਿਆਲਾ ਨੇ ਪਰਾਲੀ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਇੱਕ ਨਵੀਂ ਸੇਵਾ ਲੈ ​​ਕੇ ਆਈ ਹੈ।")
print("ਮੈਂ ਕਿਸਾਨ ਮਿੱਤਰ ਚੈਟਬੋਟ ਹਾਂ। ਮੈਂ ਤੁਹਾਨੂੰ ਪਰਾਲੀ ਸਾੜਨ ਵਰਗੇ ਤਰੀਕਿਆਂ ਅਤੇ ਤੁਹਾਡੇ ਨੇੜੇ ਉਪਲਬਧ ਹੋਰ ਸੇਵਾਵਾਂ ਬਾਰੇ ਸੂਚਿਤ ਕਰਾਂਗਾ।")

print("ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਜ਼ਿਲਾ ਚੁਣੋ:")
print("1. ਪਟਿਆਲਾ")
print("2. ਹੋਰ")
print("3. ਬੋਟ ਬੰਦ ਕਰਨ ਲਈ")

while True:
    user_input = input("ਤੁਸੀਂ: ")
    
    print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {user_input}")
    
    bot_response = respond_to_input(user_input)
    print(f"ਬੋਟ: {bot_response}")

    if user_input == "1":
        print("ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਬਲਾਕ ਚੁਣੋ")
        print("1. ਪਟਿਆਲਾ")
        print("2. ਨਾਭਾ")
        print("3. ਰਾਜਪੁਰਾ")
        print("4. ਪੁਨਰਹੇੜੀ")
        print("5. ਸਨੌਰ")
        print("6. ਸਮਾਣਾ")
        print("7. ਘਨੌਰ")
        print("8. ਪਾਤੜਾਂ")
        block_input = input("ਬਲਾਕ: ")
        print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {block_input}")

        village_input = input("ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੇ ਪਿੰਡ ਚੁਣੋ:")
        print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {village_input}")
    
        name_input = input("ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਨਾਮ ਦਰਜ ਕਰੋ:")
        print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {name_input}")
        
        print("ਤੁਹਾਡੀ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ ਧੰਨਵਾਦ")

        burn_paddy_straw_input = input("ਕੀ ਤੁਸੀਂ ਝੋਣ ਦੀ ਪ੍ਰਾਲੀ ਨੂੰ ਸਾੜਦੇ ਹੋ? (ਹਾਂ/ਨਹੀਂ):")
        print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {burn_paddy_straw_input}")

        user_data["district"] = "ਪਟਿਆਲਾ"
        user_data["village"] = village_input
        user_data["name"] = name_input
        user_data["burn_paddy_straw"] = burn_paddy_straw_input

        if user_data["burn_paddy_straw"].lower() == "yes":
            print("ਮੈਂ ਸਮਝਦਾ ਹਾਂ ਕਿ ਤੁਹਾਡੀ ਕੋਈ ਮਜਬੂਰੀ ਜ਼ਰੂਰ ਹੋਵੇਗੀ ਪਰ ਤੁਸੀਂ ਝੋਨੇ ਦੀਆਂ ਛੋਟੀਆਂ ਪੱਕਣ ਵਾਲੀਆਂ ਕਿਸਮਾਂ ਬੀਜ ਸਕਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਦੀ ਸਾਂਭ-ਸੰਭਾਲ ਆਸਾਨ ਹੈ |")
        elif user_data["burn_paddy_straw"].lower() == "no":
            print("ਜ਼ਿਲ੍ਹਾ ਪ੍ਰਸ਼ਾਸਨ ਪਟਿਆਲਾ ਤੁਹਾਡੇ ਫਾਰਮ ਲਈ ਤੁਹਾਡੇ ਯੋਗਦਾਨ ਦੀ ਸ਼ਲਾਘਾ ਕਰਦਾ ਹੈ।")
            break

        make_straw_bales_input = input("ਕੀ ਤੁਸੀਂ ਬੇਲਰ ਰਾਹੀਂ ਆਪਣੇ ਖੇਤ ਵਿੱਚ ਪ੍ਰਾਲੀ ਦਿਆਂ ਗਠਾਂ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ? (ਹਾਂ/ਨਹੀਂ):")
        print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {make_straw_bales_input}")

        user_data["make_straw_bales"] = make_straw_bales_input

        if user_data["make_straw_bales"].lower() == "yes":
            harvest_month_input = input("ਮੈਂ ਜਾਣਨਾ ਚਾਹੁੰਦਾ ਹਾਂ ਕਿ ਤੁਸੀਂ ਕਿਸ ਮਹੀਨੇ ਵਿੱਚ ਝੋਣੇ ਦੀ ਕਟਾਈ ਕਰੋਗੇ (ਸਤੰਬਰ ਅਕਤੂਬਰ ਨਵੰਬਰ ਦਸੰਬਰ):")
            print(f"ਤੁਸੀਂ ਦਿੱਤਾ: {harvest_month_input}")
            user_data["harvest_month"] = harvest_month_input
            print("ਕੀ ਤੁਸੀਂ ਸੁਪਰ ਸੀਡਰ ਜਾਂ ਕਿਸੇ ਹੋਰ ਮਸ਼ੀਨ ਨਾਲ ਆਪਣੇ ਖੇਤ ਵਿੱਚ ਪਰਾਲੀ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?")
            additional_info_input = input("(ਹਾਂ/ਨਹੀਂ):")

            if additional_info_input.lower() == "yes":
                print("ਜੇ ਤੁਸੀਂ ਆਪਣੇ ਬਲਾਕ ਵਿੱਚ ਮਸ਼ੀਨ ਦੀ ਜਾਣਕਾਰੀ ਦਿਖਾਣਾ ਚਾਹੁੰਦੇ ਹੋ, 1 ਦਬਾਓ.")
                print("ਜੇ ਤੁਸੀਂ ਪ੍ਰਾਲੀ ਬਰਤਨ ਦੇ ਵੀਡੀਓ ਦੇਖਣਾ ਚਾਹੁੰਦੇ ਹੋ, 2 ਦਬਾਓ.")
                print("ਜੇ ਤੁਸੀਂ ਬੋਟ ਲੂਪ ਤੋਂ ਬਾਹਰ ਨਿਕਲਣਾ ਚਾਹੁੰਦੇ ਹੋ, 3 ਦਬਾਓ.")

                additional_info_input = input("ਤੁਹਾਨੂੰ ਦੀ ਚੋਣ: ")

                if additional_info_input == "1":
                    # ਆਪਣੇ ਬਲਾਕ ਵਿੱਚ ਮਸ਼ੀਨ ਦੀ ਜਾਣਕਾਰੀ ਦਿਖਾਉਣ ਲਈ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ
                    print("ਇਥੇ ਤੁਹਾਡੇ ਬਲਾਕ ਵਿੱਚ ਮਸ਼ੀਨਾਂ ਦੀ ਜਾਣਕਾਰੀ ਹੈ.")
                    print("List That will be shared soon")
                    # ਮਸ਼ੀਨਰੀ ਲਿਸਟ ਦਿਖਾਉਣ ਲਈ ਆਪਣੀ ਕੋਡ ਜੋੜੋ
                elif additional_info_input == "2":
                    # ਪ੍ਰਾਲੀ ਬਰਤਨ ਦੇ ਵੀਡੀਓ ਦੀ ਜਾਣਕਾਰੀ ਦਿਖਾਉਣ ਲਈ ਕੋਡ ਜੋੜੋ
                    print("ਇਥੇ ਪ੍ਰਾਲੀ ਬਰਤਨ ਦੇ ਵੀਡੀਓਜ਼ ਦੀ ਜਾਣਕਾਰੀ ਹੈ.")
                    print("send Video!!!")
                    # ਪ੍ਰਾਲੀ ਬਰਤਨ ਵੀਡੀਓਜ਼ ਦਿਖਾਉਣ ਲਈ ਆਪਣੀ ਕੋਡ ਜੋੜੋ
                elif additional_info_input == "3":
                    print("ਬੋਟ ਲੂਪ ਤੋਂ ਬਾਹਰ ਨਿਕਲਣ ਲਈ 3 ਦਬਾਓ")
                    break
                else:
                    print("ਗਲਤ ਚੋਣ। ਕਿਰਪਾ ਕਰਕੇ ਸਹੀ ਚੋਣ ਦਰਜ ਕਰੋ (1, 2, 3)।")

    elif user_input.lower() == "exit" or user_input == "3":
        print("ਬੋਟ: ਅਲਵਿਦਾ!")
        break