from ijones.hall import Hall


def main():
    path = "resources/"

    # Initial hall

    hall = Hall(path + "ijones.in")
    hall.get_all_unique_paths()

    # Hall 1

    hall1 = Hall(path + "ijones1.in")
    hall1.get_all_unique_paths()

    # Hall 2

    hall2 = Hall(path + "ijones2.in")
    hall2.get_all_unique_paths()

    # Hall 3

    hall3 = Hall(path + "ijones3.in")
    hall3.get_all_unique_paths()


if __name__ == '__main__':
    main()
