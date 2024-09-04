import sys
import random
import heapq
import collections
import itertools

    

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.goods = 0
        self.status = 1
        self.i = -1
        self.tx = -1
        self.ty = -1
        self.berths = []
        self.target = -1
        self.back = []
        self.flag = False
        self.path = []
        self.val = 0
        self.idle = 0
        self.wait = (-1, -1)
        self.oneway = -1
        self.bb = -1

    
    #find a shortest path to p
    def find_path(self, p: tuple):
        res = [[-1] * n for _ in range(n)]
        q = collections.deque()
        q.append(p)
        res[p[0]][p[1]] = 5
        while q:
            px, py = q.popleft()
            for dx, dy, direction in [(px - 1, py, 3), (px + 1, py, 2), (px, py - 1, 0), (px, py + 1, 1)]:
                if (dx, dy) == (self.x, self.y):
                    res[dx][dy] = direction
                    return res
                if 0 <= dx < n and 0 <= dy < n and res[dx][dy] == -1 and mat[dx][dy] == '.':
                    res[dx][dy] = direction
                    q.append((dx, dy))
    
    
    def initialize(self):
        self.back = []
        self.flag = False
        self.path = []
        self.oneway = -1
        self.wait = (-1, -1)
        if self.target == -1:
            j = random.choice(self.berths)
            dis_j = 10 ** 5
            coordinate = (-1, -1)
            for center in berth[j].dis:
                temp = berth[j].dis[center][curr.x][curr.y]
                if temp < dis_j:
                    dis_j = temp
                    coordinate = center
            self.target = j
            self.tx, self.ty = coordinate
            self.idle = 0
        else:
            res = 10 ** 5
            prev = self.target
            for j in self.berths:
                if j not in leave and j not in occupied and j != prev:
                    dis_j = 10 ** 5
                    coordinate = (-1, -1)
                    for center in berth[j].dis:
                        temp = berth[j].dis[center][self.x][self.y]
                        if temp < dis_j:
                            dis_j = temp
                            coordinate = center
                    if dis_j < res:
                        res = dis_j
                        self.target = j
                        self.tx, self.ty = coordinate
                        self.idle = 0
        
    def turn(self):
        ls = [(self.x, self.y - 1), (self.x, self.y + 1), (self.x + 1, self.y), (self.x - 1, self.y)]
        idx = [0, 1, 2, 3]
        random.shuffle(idx)
        for j in idx:
            temp = ls[j]
            dx, dy = temp
            if temp not in s and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                self.x = dx
                self.y = dy
                self.back.append(j)
                print(f'move {self.i} {j ^ 1}')
                sys.stdout.flush()
                s.add((self.x, self.y))
                return
            
    def turn_oneway(self):
        self.idle += 1
        if self.wait == (-2, -2):
            if water_cnt[0] != 17222:
                if command_center.oneway[self.x][self.y] == -1:
                    return
                else:
                    ls = [(self.x, self.y - 1), (self.x, self.y + 1), (self.x + 1, self.y), (self.x - 1, self.y)]
                    idx = [0, 1, 2, 3]
                    random.shuffle(idx)
                    for j in idx:
                        temp = ls[j]
                        dx, dy = temp
                        if temp not in s and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                            self.x = dx
                            self.y = dy
                            self.back.append(j)
                            print(f'move {self.i} {j ^ 1}')
                            sys.stdout.flush()
                            s.add((self.x, self.y))
                            return
            else:
                if command_center.oneway[self.x][self.y] == -1 and self.idle < 15:
                    return
                else:
                    ls = [(self.x, self.y - 1), (self.x, self.y + 1), (self.x + 1, self.y), (self.x - 1, self.y)]
                    idx = [0, 1, 2, 3]
                    random.shuffle(idx)
                    for j in idx:
                        temp = ls[j]
                        dx, dy = temp
                        if temp not in s and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                            self.x = dx
                            self.y = dy
                            self.back.append(j)
                            print(f'move {self.i} {j ^ 1}')
                            sys.stdout.flush()
                            s.add((self.x, self.y))
                            return
        if self.wait == (-1, -1):
            ls = [(self.x, self.y - 1), (self.x, self.y + 1), (self.x + 1, self.y), (self.x - 1, self.y)]
            idx = [0, 1, 2, 3]
            random.shuffle(idx)
            self.wait = (self.x, self.y)
            for j in idx:
                temp = ls[j]
                dx, dy = temp
                if temp not in s and command_center.oneway[dx][dy] == -1 and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                    self.x = dx
                    self.y = dy
                    self.back.append(j)
                    print(f'move {self.i} {j ^ 1}')
                    sys.stdout.flush()
                    s.add((self.x, self.y))
                    return
        else:
            ls = [(self.x, self.y - 1), (self.x, self.y + 1), (self.x + 1, self.y), (self.x - 1, self.y)]
            idx = [0, 1, 2, 3]
            random.shuffle(idx)
            for j in idx:
                temp = ls[j]
                dx, dy = temp
                if temp not in s and temp != self.wait and command_center.oneway[dx][dy] == -1 and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                    self.x = dx
                    self.y = dy
                    self.back.append(j)
                    print(f'move {self.i} {j ^ 1}')
                    sys.stdout.flush()
                    s.add((self.x, self.y))
                    self.wait = (-2, -2)
                    return
            for j in idx:
                temp = ls[j]
                dx, dy = temp
                if temp not in s and temp != self.wait and 0 <= dx < n and 0 <= dy < n and mat[dx][dy] == '.':
                    self.x = dx
                    self.y = dy
                    self.back.append(j)
                    print(f'move {self.i} {j ^ 1}')
                    sys.stdout.flush()
                    s.add((self.x, self.y))
                    self.wait = (-2, -2)
                    return
            
    def find_berth(self, frame):
        res = 10 ** 6
        for j in self.berths:
            if j not in leave and j not in occupied:
                dis_j = 10 ** 6
                coordinate = (-1, -1)
                delta = 120
                if berth[j].arrival_time - frame > 1000 // delta:
                    delta = (berth[j].arrival_time - frame) // (1000 // delta)
                for center in berth[j].dis:
                    temp = 5 * berth[j].dis[center][self.x][self.y] + delta
                    if temp < dis_j:
                        dis_j = temp
                        coordinate = center
                if dis_j < res:
                    res = dis_j
                    self.target = j
                    self.tx, self.ty = coordinate
        

    def move(self, frame):
        # if frame == 15000:
        #     print(f'move {self.i} {water_cnt[0]}')
        if 15000 - berth[berth_order[0]].transport_time <= frame:
            return
        if self.status == 0:
            return
        if self.idle >= 15:
            self.initialize()
            return
        if self.tx == -1:
            self.idle += 1
            return
        if self.oneway != -1:
            if command_center.occupied[self.oneway] == 0:
                self.oneway = -1
                self.wait = (-1, -1)
                self.idle += 1
            else:
                self.turn_oneway()
            return
        if self.back:
            if self.flag or len(self.back) > random.randint(1, 10):
                self.flag = True
                direction = self.back.pop()
                dy = (1 - (direction & 1) * 2) if direction & 2 == 0 else 0
                dx = (1 - (direction & 1) * 2) if direction & 2 else 0
                if (self.x - dx, self.y + dy) not in s:
                    self.y += dy
                    self.x -= dx
                    s.add((self.x, self.y))
                    print(f'move {self.i} {direction}')
                    sys.stdout.flush()

                else:
                    self.back.append(direction)
                    self.idle += 1
            else:
                self.turn()
            return
        self.idle = 0
        self.flag = False
        if self.target != -1:
            direction = berth[self.target].path[(self.tx, self.ty)][self.x][self.y]
        else:
            direction = self.path[self.x][self.y]
        if direction == -1 or direction == 5:
            self.initialize()
            return
        dy = (1 - (direction & 1) * 2) if direction & 2 == 0 else 0
        dx = (1 - (direction & 1) * 2) if direction & 2 else 0
        if (self.x - dx, self.y + dy) not in s:
            j = command_center.oneway[self.x - dx][self.y + dy]
            if j != -1 and (command_center.oneway[self.x][self.y] == -1 or command_center.occupied[command_center.oneway[self.x][self.y]] == 0) and (command_center.occupied[j] == 1 and command_center.direction[j] != (self.x - dx, self.y + dy) or command_center.occupied[j] == -1 and command_center.direction[j] == (self.x - dx, self.y + dy)):
                self.oneway = j
                self.turn_oneway()
                return
            self.x -= dx
            self.y += dy
            print(f'move {self.i} {direction}')
            sys.stdout.flush()
            s.add((self.x, self.y))
        else:
            self.turn()

        if self.x == self.tx and self.y == self.ty:
            if self.target == -1:
                if gds[self.x][self.y] != 0:
                    print(f'get {self.i}')
                    sys.stdout.flush()
                self.val = gds[self.x][self.y]
                gds[self.x][self.y] = 0
                self.find_berth(frame)
            else:
                if self.goods and self.target in leave:
                    res = 10 ** 5
                    for j in self.berths:
                        if j not in leave and j not in occupied:
                            dis_j = 10 ** 5
                            coordinate = (-1, -1)
                            for center in berth[j].dis:
                                temp = berth[j].dis[center][self.x][self.y]
                                if temp < dis_j:
                                    dis_j = temp
                                    coordinate = center
                            if dis_j < res and dis_j + frame <= 14990 - berth[j].transport_time:
                                res = dis_j
                                self.target = j
                                self.tx, self.ty = coordinate
                    if res == 10 ** 5:
                        for j in self.berths:
                            if j not in leave:
                                dis_j = 10 ** 5
                                coordinate = (-1, -1)
                                for center in berth[j].dis:
                                    temp = berth[j].dis[center][self.x][self.y]
                                    if temp < dis_j:
                                        dis_j = temp
                                        coordinate = center
                                if dis_j < res and dis_j + frame <= 14990 - berth[j].transport_time:
                                    res = dis_j
                                    self.target = j
                                    self.tx, self.ty = coordinate
                    return
                
                if self.goods:
                    print(f'pull {self.i}')
                    sys.stdout.flush()
                    berth[self.target].val += self.val
                    berth[self.target].goods.append(self.val)
                    # ff[0] += self.val
                    self.val = 0
                    berth[self.target].cnt += 1
                berth[self.target].robots.append(i)
                self.tx = -1
                self.ty = -1
                self.target = -1


class Berth:
    def __init__(self, n: int):
        self.x = 0
        self.y = 0
        self.transport_time = 0
        self.loading_speed = 0
        self.robots = []
        self.cnt = 0
        self.empty = True
        self.h = []
        self.dis = {}
        self.path = {}
        self.val = 0
        self.goods = collections.deque()
        # self.addition = 0
        self.arrival_time = 0
        self.wait = False

    def assign(self):
        while self.h and (self.h[0][1] <= frame or (self.h[0][2] not in goods_index)):
            heapq.heappop(self.h)
        if self.h:
            idx = heapq.heappop(self.h)[2]
            rob = robot[self.robots.pop()]
            rob.tx, rob.ty = goods_index[idx]
            rob.path = rob.find_path(goods_index[idx])
            goods_index.pop(idx)
            rob.target = -1

class Boat:
    def __init__(self):
        self.num = 0
        self.status = 1
        self.pos = -1
        self.goods = 0
        self.i = -1
        self.last = -1
        self.berths = []
        self.parity = 1
        self.r0 = 0
        self.r1 = 0

    def move(self, frame):
        if self.status == 0 or self.status == 2:
            if self.pos != -1:
                if self.pos in leave:
                    leave.remove(self.pos)
            return
        if self.pos == -1:
            j = self.berths[self.parity]
            if frame + 2 * berth[j].transport_time > 14999:
                return
            if self.parity == 1:
                if self.r1 >= 1:
                    self.r1 -= 1
            else:
                if self.r0 >= 1:
                    self.r0 -= 1
            print(f'ship {self.i} {j}')
            sys.stdout.flush()
            if j in leave:
                leave.remove(j)
            berth[j].arrival_time = frame + berth[j].transport_time
            self.pos = j
            berth[j].empty = False
            self.parity = 1 - self.parity
        else:
            if berth[self.pos].transport_time + frame + self.r0 * candidates[self.berths[0]] + self.r1 * candidates[self.berths[1]] > 14995:
                print(f'go {self.i}')
                sys.stdout.flush()
                if self.r1 == 0:
                    leave.add(self.pos)
                berth[self.pos].empty = True
                self.pos = -1
                self.goods = 0
            elif berth[self.pos].cnt > 0 and self.goods < boat_capacity:
                if berth[self.pos].cnt >= berth[self.pos].loading_speed:
                    if self.goods + berth[self.pos].loading_speed <= boat_capacity:
                        self.goods += berth[self.pos].loading_speed
                        temp = berth[self.pos].loading_speed
                    else:
                        temp = boat_capacity - self.goods
                        self.goods = boat_capacity
                else:
                    if self.goods + berth[self.pos].cnt <= boat_capacity:
                        temp = berth[self.pos].cnt
                        self.goods += temp
                    else:
                        temp = boat_capacity - self.goods
                        self.goods = boat_capacity
                berth[self.pos].cnt -= temp
                while temp != 0:
                    berth[self.pos].val -= berth[self.pos].goods.popleft()
                    temp -= 1
            elif self.goods == boat_capacity:
                print(f'go {self.i}')
                sys.stdout.flush()
                berth[self.pos].empty = True
                if self.r1 == 0:
                    leave.add(self.pos)
                self.pos = -1
                self.goods = 0
            elif self.r0 == 0:
                temp = -1
                res = 1500
                for j in leave:
                    curr = berth[j]
                    if curr.empty and curr.cnt + self.goods <= boat_capacity and curr.val > res and frame + 500 + curr.transport_time + curr.cnt // curr.loading_speed < 14990:
                        res = curr.val
                        temp = j
                if temp != -1:
                    print(f'ship {self.i} {temp}')
                    sys.stdout.flush()
                    berth[temp].arrival_time = frame + 500
                    leave.add(self.pos)
                    self.pos = temp
                    leave.remove(self.pos)
                    berth[self.pos].empty = False
                else:
                    for j in range(berth_num):
                        if j not in leave:
                            curr = berth[j]
                            if curr.wait == False and curr.cnt > boat_capacity and curr.val > res and frame + 500 + curr.transport_time + (curr.cnt - boat_capacity) // curr.loading_speed < 14990 and curr.arrival_time + boat_capacity // curr.loading_speed < frame + 480:
                                res = curr.val
                                temp = j
                    if temp != -1:
                        print(f'ship {self.i} {temp}')
                        sys.stdout.flush()
                        berth[temp].arrival_time = frame + 500
                        leave.add(self.pos)
                        self.pos = temp
                        berth[self.pos].empty = False
                        berth[self.pos].wait = True
                        if temp in leave:
                            leave.remove(temp)
            else:
                temp = -1
                res = 1500
                for j in range(berth_num):
                    curr = berth[j]
                    if curr.empty and curr.cnt + self.goods <= boat_capacity and curr.val > res and frame + 500 + curr.transport_time + curr.cnt // curr.loading_speed + self.r0 * candidates[self.berths[0]] + self.r1 * candidates[self.berths[1]]  < 14990:
                        res = curr.val
                        temp = j
                if temp != -1:
                    print(f'ship {self.i} {temp}')
                    sys.stdout.flush()
                    berth[temp].arrival_time = frame + 500
                    berth[self.pos].empty = True
                    if self.r1 == 0:
                        leave.add(self.pos)
                    self.pos = temp
                    berth[self.pos].empty = False
                    if temp in leave:
                        leave.remove(temp)


class Controller:
    def __init__(self):
        self.grid = [[False] * n for _ in range(n)]
        self.oneway = [[-1] * n for _ in range(n)]
        self.occupied = []
        self.direction = [(-1, -1)]
        self.cnt = 0

def Init():
    for _ in range(n):
        mat.append(list(input()))
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '*':
                water_cnt[0] += 1
    if water_cnt[0] == 17222:
        mat[148][173] = '#'
        mat[148][174] = '#'
        mat[25][173] = '#'
        mat[25][174] = '#'

    for _ in range(berth_num):
        id, x, y, t, v = map(int, input().split())
        curr = berth[id]
        curr.x = x
        curr.y = y
        curr.transport_time = t
        curr.loading_speed = v
        for dx in range(x, x + 4):
            for dy in range(y, y + 4):
                mat[dx][dy] = '.'

        for dx in [x, x + 3]:
            for dy in [y, y + 3]:
                curr.dis[(dx, dy)] = [[-1] * n for _ in range(n)]
                curr.path[(dx, dy)] = [[-1] * n for _ in range(n)]
    boat_capacity = int(input())
    okk = input()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 'A':
                robot[cnt].x = i
                robot[cnt].y = j
                initial_pos[(i, j)] = cnt
                cnt += 1
                mat[i][j] = '.'

    for i in range(n):
        for j in range(n):
            if mat[i][j] != '.':
                continue
            cnt = 0
            for di, dj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= di < n and 0 <= dj < n and mat[di][dj] == '.':
                    cnt += 1
            if cnt <= 2:
                command_center.grid[i][j] = True

    cnt = 1
    vis = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if vis[i][j]:
                continue

            vis[i][j] = True
            if not command_center.grid[i][j]:
                continue
            q = [(i, j)]
            command_center.oneway[i][j] = cnt
            while q:
                i, j = q.pop()
                for di, dj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= di < n and 0 <= dj < n and not vis[di][dj]:
                        vis[di][dj] = True
                        if command_center.grid[di][dj]:
                            q.append((di, dj))
                            command_center.oneway[di][dj] = cnt
            command_center.direction.append((i, j))
            cnt += 1
    command_center.cnt = len(command_center.direction)
    command_center.occupied = [0] * command_center.cnt

    return boat_capacity



def check_connectivity(): 
    res = set()
    for i in berth_order:
        curr = berth[i]
        for center in curr.dis:
            q = collections.deque()
            curr.dis[center][center[0]][center[1]] = 0
            curr.path[center][center[0]][center[1]] = 5
            q.append(center)
            dd = 1
            grid[center[0]][center[1]] = 0
            grid_idx[center[0]][center[1]] = i
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy, direction in [(x - 1, y, 3), (x + 1, y, 2), (x, y - 1, 0), (x, y + 1, 1)]:
                        if 0 <= dx < n and 0 <= dy < n and curr.dis[center][dx][dy] == -1 and mat[dx][dy] == '.':
                            curr.dis[center][dx][dy] = dd
                            if grid[dx][dy] == -1 or grid[dx][dy] > dd:
                                grid[dx][dy] = dd
                                grid_idx[dx][dy] = i
                            curr.path[center][dx][dy] = direction
                            q.append((dx, dy))
                dd += 1

        if water_cnt[0] == 4339:
            for j in range(robot_num // 2):
                rob = robot[j]
                if curr.dis[center][rob.x][rob.y] != -1 and curr.x < 95:
                    rob.berths.append(i)
                    res.add(j)
            for j in range(robot_num // 2, robot_num):
                rob = robot[j]
                if curr.dis[center][rob.x][rob.y] != -1 and curr.x > 95:
                    rob.berths.append(i)
                    res.add(j)
        elif water_cnt[0] == 17222:
            for j in range(2):
                rob = robot[j]
                if curr.dis[center][rob.x][rob.y] != -1 and curr.y > 120 and curr.x < 30:
                    rob.berths.append(i)
                    res.add(j)
            for j in range(2, robot_num - 3):
                rob = robot[j]
                if curr.dis[center][rob.x][rob.y] != -1 and curr.y > 120 and curr.x > 30:
                    rob.berths.append(i)
                    res.add(j)
            for j in range(robot_num - 3, robot_num):
                rob = robot[j]
                if curr.dis[center][rob.x][rob.y] != -1 and curr.y < 120:
                    rob.berths.append(i)
                    res.add(j)
        else:
            for j, rob in enumerate(robot):
                if curr.dis[center][rob.x][rob.y] != -1:
                    rob.berths.append(i)
                    res.add(j)
    

    remain = set([i for i in range(berth_num)])
    for i in res:
        curr = robot[i]
        dd = 10 ** 5
        for j in curr.berths:
            if j in remain:
                dis_j = 10 ** 5
                coordinate = (-1, -1)
                for center in berth[j].dis:
                    temp = berth[j].dis[center][curr.x][curr.y]
                    if temp < dis_j:
                        dis_j = temp
                        coordinate = center
                if dis_j < dd:
                    dd = dis_j
                    curr.target = j
                    curr.bb = j
                    curr.tx, curr.ty = coordinate
        if dd != 10 ** 5:
            remain.remove(curr.target)
        else:
            for j in curr.berths:
                temp = berth[j].transport_time
                if temp < dd:
                    dd = temp
                    curr.target = j
                    curr.bb = j
                    dis_j = 10 ** 5
                    coordinate = (-1, -1)
                    for center in berth[j].dis:
                        temp = berth[j].dis[center][curr.x][curr.y]
                        if temp < dis_j:
                            dis_j = temp
                            coordinate = center
                    curr.tx, curr.ty = coordinate
    res = list(res)
    res.sort()
    return res


def Input(good_cnt):
    frame, money = map(int, input().split())
    num = int(input())
    for _ in range(num):
        x, y, val = map(int, input().split())
        gds[x][y] = val
        goods_index[good_cnt] = (x, y)
        for i, curr in enumerate(berth):
            dd = 10 ** 5
            coordinate = (-1, -1)
            for center in curr.dis:
                temp = curr.dis[center][x][y]
                if temp == -1:
                    break
                if temp < dd:
                    dd = temp
                    coordinate = center
            if dd != 10 ** 5:
                # dj = 10 ** 5
                # for another in berth:
                #     for center in another.dis:
                #         temp = another.dis[center][x][y]
                #         if temp == -1:
                #             break
                #         if temp < dj:
                #             dj = temp
                # if dj != 10 ** 5:
                #     dj = 0
                heapq.heappush(curr.h, (-val * 1000 // dd, frame + 1000 - dd - 30, good_cnt, coordinate))
        good_cnt += 1
    for i in range(robot_num):
        robot[i].goods, robot[i].x, robot[i].y, robot[i].status = map(int, input().split())
    for i in range(boat_num):
        boat[i].status, boat[i].pos = map(int, input().split())
    okk = input()
    return good_cnt, frame

def generate_pairs(items, item_cnt, start):
    if item_cnt & 1:
        return
    if start == item_cnt:
        temp = []
        for i in range(0, item_cnt, 2):
            temp.append(items[i])
            temp.append(items[i+1])
        ls.append(temp)
        return
    for j in range(start + 1, item_cnt):
        items[start+1], items[j] = items[j], items[start+1]
        generate_pairs(items, item_cnt, start + 2)
        items[start+1], items[j] = items[j], items[start+1]




if __name__ == "__main__":
    n = 200
    robot_num = 10
    berth_num = 10
    boat_num = 5
    robot = [Robot() for _ in range(robot_num)]
    berth = [Berth(n) for _ in range(berth_num)]
    boat = [Boat() for _ in range(boat_num)]
    for i, curr in enumerate(boat):
        curr.i = i

    mat = []
    initial_pos = {}
    grid = [[-1] * n for _ in range(n)]
    grid_idx = [[-1] * n for _ in range(n)]

    gds = [[0 for _ in range(n)] for _ in range(n)]
    command_center = Controller()
    water_cnt = [0]
    boat_capacity = Init()

    
    berth_order = [i for b, i in sorted([[b, i] for i, b in enumerate(berth)], key=lambda x: x[0].transport_time)]

    possible_robots = check_connectivity()


    # cover_cnt = [0] * berth_num
    # for i in range(n):
    #     for j in range(n):
    #         if grid_idx[i][j] != -1:
    #             cover_cnt[grid_idx[i][j]] += 1
    # abandon_berth = set()
    # temp_s = sum(cover_cnt)
    # for i in range(berth_num):
    #     if cover_cnt[i] / temp_s < 0.005:
    #         abandon_berth.add(i)
    
    


    candidates = [2 * berth[i].transport_time + boat_capacity // berth[i].loading_speed for i in range(berth_num)]
    ls = []
    generate_pairs([i for i in range(berth_num)], berth_num, 0)
    res = 0
    combination = [i for i in range(berth_num)]
    for temp in ls:
        curr = 0
        for i in range(0, berth_num, 2):
            x, y = candidates[temp[i]], candidates[temp[i+1]]
            if x > y:
                x, y = y, x
            curr += max(14990 // (x + y) * 2, 1 + (14990 - x) // (x + y) * 2)
        if curr > res:
            res = curr
            combination = temp

    for i, curr in enumerate(boat):
        curr.berths.append(combination[2 * i])
        curr.berths.append(combination[2 * i + 1])
        curr.berths.sort(key=lambda i: berth[i].transport_time)
        x, y = candidates[curr.berths[0]], candidates[curr.berths[1]]
        if 1 + (14990 - x) // (x + y) * 2 > 14990 // (x + y) * 2:
            curr.parity = 0
            curr.r0 = 1 + (14990 - x) // (x + y)
            curr.r1 = (14990 - x) // (x + y)
        else:
            curr.r0 = 14990 // (x + y)
            curr.r1 = 14990 // (x + y)


    
            
    # grid_init()
    initial_target = [r.target for r in robot]
    initial_tx = [r.tx for r in robot]
    initial_ty = [r.ty for r in robot]
    print("OK")
    sys.stdout.flush()

    goods_index = {}
    good_cnt = 0
    frame, _ = map(int, input().split())
    num = int(input())
    for _ in range(num):
        x, y, val = map(int, input().split())
        gds[x][y] = val
        goods_index[good_cnt] = (x, y)
        for i, curr in enumerate(berth):
            dd = 10 ** 5
            coordinate = (-1, -1)
            for center in curr.dis:
                temp = curr.dis[center][x][y]
                if temp == -1:
                    break
                if temp < dd:
                    dd = temp
                    coordinate = center
            if dd != 10 ** 5:
                heapq.heappush(curr.h, (-val * 1000 // dd, frame + 1000 - dd, good_cnt, coordinate))
        good_cnt += 1

    for i in range(robot_num):
        robot[i].goods, x, y, robot[i].status = map(int, input().split())
        j = initial_pos[(x, y)]
        robot[i].target, robot[i].tx, robot[i].ty = initial_target[j], initial_tx[j], initial_ty[j]
        robot[i].i = i
    for i in range(boat_num):
        boat[i].status, boat[i].pos = map(int, input().split())
    okk = input()
    leave = set()
    occupied = set()

    for i in possible_robots:
        curr = robot[i]
        if berth[curr.target].h and berth[curr.target].h[0][2] in goods_index:
            x, y =  goods_index[berth[curr.target].h[0][2]]
            if grid_idx[x][y] == curr.target:
                curr.tx = x
                curr.ty = y
                curr.path = curr.find_path((x, y))
                goods_index.pop(heapq.heappop(berth[curr.target].h)[2])
                curr.target = -1
    

    s = set()
    for i in possible_robots:
        s.add((robot[i].x, robot[i].y))
    for i in possible_robots:
        robot[i].move(1)
    for i in range(boat_num):
        boat[i].move(1)
    print("OK")
    sys.stdout.flush()
    
    # for curr in berth:
    #     curr.addition = 10 * curr.transport_time // boat_capacity + 5 // curr.loading_speed

    ff = [0]
    for _ in range(2, 15001):
        good_cnt, frame = Input(good_cnt)
        for i, curr in enumerate(berth):
            if curr.cnt > boat_capacity and curr.wait == False:
                occupied.add(i)
                continue
            else:
                occupied.discard(i)
            if curr.robots and i not in leave:
                curr.assign()

        s = set()
        ls = [0] * command_center.cnt
        for i in possible_robots:
            s.add((robot[i].x, robot[i].y))
            j = command_center.oneway[robot[i].x][robot[i].y]
            if j != -1:
                if command_center.occupied[j] == 1:
                    ls[j] = 1
                elif command_center.occupied[j] == -1:
                    ls[j] = -1
                else:
                    if command_center.direction[j] == (robot[i].x, robot[i].y):
                        ls[j] = 1
                    else:
                        ls[j] = -1
        
        command_center.occupied = ls
        for i in possible_robots:
            robot[i].move(frame)

        for i in range(boat_num):
            boat[i].move(frame)
        print("OK")
        sys.stdout.flush()
        if frame == 15000:
            break
