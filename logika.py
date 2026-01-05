ploca = [['.' for _ in range(8)] for _ in range(8)]
#ploca: list[list[chr]] = [
#    ['.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '.', '.', '.'], 
#     ['O', '.', '.', '.', '.', '.', '.', '.'] 
#]
na_potezu = True

def __enemy_of__(point: chr) -> chr:
    if point == 'O':   return 'X'
    elif point == 'X': return 'O'
    else: return '.'

def __translate__(potez: str) -> tuple[int, int]:
    return (8-int(potez[1]), ord(potez[0])-97)

def __procitaj__(potez: tuple[int, int]) -> chr:
    return ploca[potez[0]][potez[1]]

def __good__(coor: tuple[int, int]) -> bool:
    return (coor[0] >= 0 and coor[0] <= 7 and coor[1] >= 0 and coor[1] <= 7)

visited: list[tuple[int, int]] = []
def __visitable__(location: tuple[int, int], enemy: chr, first_time = True) -> None:
    global visited
    if first_time: visited = []
    if location in visited: return
    y, x = location
    visited.append(location)
    for xoff in [-2, 2]:
        for yoff in [-2, 2]:
            dx = x+xoff
            dy = y+yoff
            if (dx < 0 or dx > 7 or dy < 0 or dy > 7): continue
            if (__procitaj__((dy, dx)) != '.'): continue
            if (__procitaj__((y+yoff//2, x+xoff//2)) != enemy): continue 
            __visitable__((dy, dx), enemy, False)

def validan_potez(pocetak: str, kraj: str) -> bool:
    pocetak = __translate__(pocetak)
    kraj = __translate__(kraj)
    if (not __good__(pocetak) or not __good__(kraj)): return False
    if __procitaj__(pocetak) == '.' or __procitaj__(kraj) != '.': return False
    if (na_potezu and __procitaj__(pocetak) == 'X') or (not na_potezu and __procitaj__(pocetak) == 'O'): return False
    
    if (kraj[0]-pocetak[0] == 1 and abs(kraj[1]-pocetak[1]) == 1): return True
    __visitable__(pocetak, __enemy_of__(__procitaj__(pocetak)))
    return (kraj in visited)

    
if __name__ == "__main__":
    print(validan_potez("a1", "c3"))
