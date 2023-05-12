class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)

    def handle_key(self, key):
        if key == pygame.K_UP and self.direction != (0, 10):
            self.direction = (0, -10)
        elif key == pygame.K_DOWN and self.direction != (0, -10):
            self.direction = (0, 10)
        elif key == pygame.K_LEFT and self.direction != (10, 0):
            self.direction = (-10, 0)
        elif key == pygame.K_RIGHT and self.direction != (-10, 0):
            self.direction = (10, 0)

    def update(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, position):
        return self.body[0] == position

    def check_wall_collision(self):
        head = self.body[0]
        return head[0] < 0 or head[0] >= 640 or head[1] < 0 or head[1] >= 480

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))
