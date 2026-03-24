from colorama import init as colorama_init, Fore, Back, Style

# Key binds
KEY_UP = 'w'		# Вверх
KEY_DOWN = 's'		# Вниз
KEY_LEFT = 'a'		# Влево
KEY_RIGHT = 'd'		# Вправо
KEY_QUIT = 'q'		# Выход из игры

# Game settings
GAME_SPEED = 3
AMOUNT_OF_FOOD = 15

# Tiles theme
themes = ['color_block', 'programm_art', 'programm_art_expanded', 'color_programm_art_expanded']
theme = themes[3]
if theme == 'color_block':
	DEFAULT_TILE = f'█'
	PLAYER_HEAD = f'{Fore.BLACK}█{Style.RESET_ALL}'
	PLAYER_TAIL = f'{Fore.RED}█{Style.RESET_ALL}'
	FOOD = f'{Fore.GREEN}█{Style.RESET_ALL}'
elif theme == 'programm_art':
	DEFAULT_TILE = '.'
	PLAYER_HEAD = f'@'
	PLAYER_TAIL = f'x'
	FOOD = f'0'
elif theme == 'programm_art_expanded':
	DEFAULT_TILE = '. '
	PLAYER_HEAD = f'@ '
	PLAYER_TAIL = f'x '
	FOOD = f'0 '
elif theme == 'color_programm_art_expanded':
	DEFAULT_TILE = f'{Fore.WHITE}.{Style.RESET_ALL} '
	PLAYER_HEAD = f'{Fore.WHITE}{Style.BRIGHT}@{Style.RESET_ALL} '
	PLAYER_TAIL = f'{Fore.RED}X{Style.RESET_ALL} '
	FOOD = f'{Fore.GREEN}{Style.BRIGHT}0{Style.RESET_ALL} '