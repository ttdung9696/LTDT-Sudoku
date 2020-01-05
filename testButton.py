# pylint: disable=no-member
import pygame


pygame.init()

WHITE = (255, 255, 255)
ACTIVE_COLOR = pygame.Color('dodgerblue1')
INACTIVE_COLOR = pygame.Color('dodgerblue4')
FONT = pygame.font.Font(None, 50)


def draw_button(button, screen):
    """Draw the button rect and the text surface."""
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    """A button is a dictionary that contains the relevant data.

    Consists of a rect, text surface and text rect, color and a
    callback function.
    """
    # The button is a dictionary consisting of the rect, text,
    # text rect, color and the callback function.
    text_surf = FONT.render(text, True, WHITE)
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': INACTIVE_COLOR,
        'callback': callback,
        }
    return button


def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    number = 0

    def increment_number():  # A callback function for the button.
        """Increment the `number` in the enclosing scope."""
        nonlocal number
        number += 1
        print(number)

    def quit_game():  # A callback function for the button.
        nonlocal done
        done = True

    button1 = create_button(100, 100, 250, 80, 'Click me!', increment_number)
    button2 = create_button(100, 200, 250, 80, 'Me too!', quit_game)
    # A list that contains all buttons.
    button_list = [button1, button2]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                print('event.button', event.button)
                if event.button == 1:
                    for button in button_list:
                        # `event.pos` is the mouse position.
                        if button['rect'].collidepoint(event.pos):
                            # Increment the number by calling the callback
                            # function in the button list.
                            button['callback']()
            elif event.type == pygame.MOUSEMOTION:
                # When the mouse gets moved, change the color of the
                # buttons if they collide with the mouse.
                for button in button_list:
                    if button['rect'].collidepoint(event.pos):
                        button['color'] = ACTIVE_COLOR
                    else:
                        button['color'] = INACTIVE_COLOR

        screen.fill(WHITE)
        for button in button_list:
            draw_button(button, screen)
        pygame.display.update()
        clock.tick(30)


main()
pygame.quit()