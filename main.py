import random
import time


eng_words = ['Hello','Hi','Bye','Task','Programm','Friend','Teacher','Knowledge','Thank you','You are welcome','Okay','Yes','No','Wait','Great']
in_words = ['Halo','Hai','Sampai jumpa','Tugas','Program','Teman','Guru','Pengetahuan','Terima kasih','Sama-sama','Oke','Iya','Tidak','Tunggu','Bagus']
score = 0

while True:
    mode = input("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                 "0 - tambahkan kata baru \n 1 - berlatih Inggris --> Indonesia \n 2 - berlatih Indonesia --> Inggris \n Pilih mode: ")
    while ((mode != '0') and (mode != '1') and (mode != '2')):
        mode = input("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Simbol tidak valid! Pilih antara 0, 1 atau 2. (0 - tambahkan kata baru, 1 - berlatih Inggris --> Indonesia, 2 - berlatih Indonesia --> Inggris): ")

    if mode == "1":
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
              "Terjemahkan kata sebanyak mungkin! Kamu punya",len(eng_words),"kesempatan!"
              "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for h in range(len(eng_words)):
            number = random.randint(0, len(eng_words)-1)
            print("Pertanyaan ke-",h+1,". Terjemahkan kata ini (gunakan huruf kapital di awal kalimat): " + eng_words[number])
            if input() == in_words[number]:
                print("Benar!!! Hebat!!!")
                score += 1
                print("Skor: ",score,
                      "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("Bukan, jawaban yang benar adalah - " + in_words[number])
                print("Skor: ",score,
                      "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Kamu menjawab benar",score,"pertanyaan dari",len(eng_words),"pertanyaan!")
    elif mode == "2":
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
              "Terjemahkan kata sebanyak mungkin! Kamu punya",len(in_words),"kesempatan!"
              "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for h in range(len(in_words)):
            number = random.randint(0, len(in_words)-1)
            print("Pertanyaan ke-",h+1,". Terjemahkan kata ini (gunakan huruf kapital di awal kalimat): " + in_words[number])
            if input() == eng_words[number]:
                print("Benar!!! Hebat!!!")
                score += 1
                print("Skor: ",score,
                      "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("Bukan, jawaban yang benar adalah - " + eng_words[number])
                print("Skor: ",score,
                      "\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Kamu menjawab benar",score,"pertanyaan dari",len(in_words),"pertanyaan!")
    else:
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        word = input("Ketik kata bahasa Inggris: ")
        translate = input("Ketik terjemahan kata ini: ")
        if len(word) > 0 and len(translate) > 0:
            eng_words.append(word)
            in_words.append(translate)
            print("Kata berhasil ditambahkan!")
