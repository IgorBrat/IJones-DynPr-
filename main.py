from ijones.hall import Hall


def main():
    hall = Hall("resources/ijones2.in")
    hall.dfs_modified((0, 0))


if __name__ == '__main__':
    main()
