from survey import Survey



lang_survei = Survey("Apa bahasa pemrograman kesukaanmu ?")

lang_survei.show_question()
print("Ketikan 'q' untuk keluar \n")

while True:
    response = input("Bahasa : ")
    if response == 'q':
        break
    lang_survei.store_response(response)

print("\n Terima kasih sudah mengikuti survey")
lang_survei.show_results()
