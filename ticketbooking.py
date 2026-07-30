print("***** Movie Ticket Booking System *****")
movie=input("Enter the movie name: ")
print("Available shows for", movie, ":")
show_times=["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]
adults=int(input("Enter number of adult tickets: "))
children=int(input("Enter number of children tickets: "))
children_5=int(input("Enter number of children below 5 years: "))
if seat == "yes":
    print("Seat selection is available.")   
else:
    print("Seat selection is not available.")
print("Booking Summary:")
print("Movie:", movie)
print("Show Time:", show_time)
print("Adult Tickets:", adults)
print("Children Tickets:", children)
print("Total Tickets:", adults + children)
print("Thank you for booking with us!")