# მაღაზიაში ფასდაკლება არის მხოლოდ არასრულოვნებზე და სტუდენტებზე.
#  არასრუწლოვანი ან სტუდენტი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი
#  ან არასტუდენტი გადაიხდის ჩვეულებრივ ფასს.
#  დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.


age = int(input("შეიყვანეთ თქვენი ასაკი: "))
is_student = input("ხართ თუ არა სტუდენტი? (დიახ/არა): ")


if age < 18 or is_student == "დიახ":
    print("თქვენ მიიღებთ 50%-იან ფასდაკლებას!")
else:
    print("თქვენ არ მიიღებთ ფასდაკლებას და გადაიხდით ჩვეულებრივ ფასს.")