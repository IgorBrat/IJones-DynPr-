from ijones.hall import Hall


def main():
    hall = Hall("resources/ijones.in")
    hall.dfs_modified((1, 0))


if __name__ == '__main__':
    main()
