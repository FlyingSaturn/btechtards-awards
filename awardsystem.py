CAP = .95
FACTOR = 2

def main():
    posters=[]
    points=0
    number=0
    print("Welcome!\n\nThis post/comment is eligible for your award.\nGive an award (name subject to change).\nNote that one user can only award a post once.\n")
    op = input("Do you want to give it an award (y/n): ")
    while op.lower() in ['y', 'yes', '1']:
        if points >= 1:
            print("Vote not incremented as limit reached.")
            show_details(points, posters)
        else:
            x = input("Name: ")
            if not eligibleposter(x):
                print("Sorry, you are not eligible for giving awards. Try again after you have all the requirements.")
                show_details(points, posters)
            elif x in posters:
                print("Sorry, same user can't reward twice.")
                show_details(points, posters)
            else:
                posters.append(x)
                points = incre(points, number, number+1)
                number = number + 1
                if (points >= 1):
                    print("Vote incremented. Limit reached.")
                else:
                    print("Vote incremented!")
                show_details(points, posters)
        op = input("Do you want to give it another award (y/n):")
    print("End result: ")
    show_details(points, posters)


# Dummy function (will contain karma requirements and such)
def eligibleposter(username):
    if username == 'duck':
        return False
    return True


# To calculate points
def calc_points(n):
    if n <= 0:
        return 0
    s = 0
    for i in range(1,n+1):
        s = s + 1/(FACTOR**i)
        if s >= CAP:
            s = 1
            break
    return s


# Just incrementing the points
def incre(total_points, old, new):
    return (total_points - calc_points(old) + calc_points(new))


# Detail showing
def show_details(point, poster):
    print("\n-----\nDetails: ")
    print("No. of points:", point)
    print("Posters: ")
    for i in poster:
        print(i)
    print("\n-----\n")


main()
