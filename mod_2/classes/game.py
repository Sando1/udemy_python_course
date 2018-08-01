import random
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEBUG = '\033[94m'


class Person:
    """
    hp : hit points
    mp : magic points
    atk : atack
    atk_l = attack low
    atk_h = attack high
    df : defense
    mgc : magic
    items = items
    """
    def __init__(self,name, hp, mp, atk, df, mgc, items):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.mgc = mgc
        self.items = items
        self.actions = ['Atack','Magic','Items']

    def generate_damage(self):
        return random.randrange(self.atk_l,self.atk_h)

    def take_damage(self, dmg):
        """
        function for player to take
        the damage
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def set_hp(self,hp):
        self.hp = hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def set_mp(self,mp):
        self.mp = mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print(bcolors.HEADER + bcolors.BOLD + '\tACTIONS' + bcolors.ENDC)
        for i,item in enumerate(self.actions):
            print('\t\t{}:{}'.format(i,item))


    def choose_magic(self):
        print(bcolors.HEADER + bcolors.BOLD + '\tMAGIC'+ bcolors.ENDC)
        for i,spell in enumerate(self.mgc):
            print(bcolors.OKBLUE +'\t\t{}:{}'.format(i, spell.name) + bcolors.ENDC)
            print('\t\tcost : ',spell.cost)

    def heal(sel, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def choose_item(self):
        print(bcolors.HEADER + bcolors.BOLD + '\tITEMS' + bcolors.ENDC)
        for i,item in enumerate(self.items):
            print(bcolors.OKBLUE + '\t\t{}:{}'.format(i,item['item'].name) + bcolors.ENDC )
            print('\t\tDescription: ', item['item'].des)
            print('\t\tQty : {}'.format(item['qty']))

    def get_stats(self):
        bar = '█'
        bar_ticks_hp = math.floor((self.hp/self.maxhp) * (100/4))
        bar_ticks_mp = math.floor((self.mp/self.maxmp) * (100/10))

        name = '{} \t '.format(self.name)
        hp   = '{}/{} '.format(self.get_hp(), self.get_max_hp()) + bcolors.OKBLUE + '|{0:<25}|\t\t'.format(bar*bar_ticks_hp)
        mp   = '{}/{} '.format(self.get_mp(), self.get_max_mp()) + bcolors.OKGREEN + '|{0:<10}|'.format(bar*bar_ticks_mp)
        print(bcolors.BOLD + name + hp + mp + '\n' + bcolors.ENDC)

    def get_enemy_stats(self):
        bar = '█'
        bar_ticks_hp = math.floor((self.hp/self.maxhp) * (100/2))

        name = '{} \t '.format(self.name)
        hp   = '{}/{} '.format(self.get_hp(), self.get_max_hp()) + bcolors.WARNING + '|{0:<50}|\t\t'.format(bar*bar_ticks_hp)
        #mp = bcolors.BOLD + '{}/{} '.format(self.get_mp, self.get_max_mp) +
           # bcolors.OKGREEN + '|{0:<10}|'.format(bar*bar_ticks_mp) + bcolors.ENDC
        print(bcolors.BOLD + name + hp +'\n'  + bcolors.ENDC)

    def choose_target(self,enemies):
        print(bcolors.HEADER + bcolors.FAIL + '\tENEMIES' + bcolors.ENDC)
        for i,enemy in enumerate(enemies):
            if enemy.get_hp() !=0:
                print('\t\t{}:{}'.format(i,enemy.name))
