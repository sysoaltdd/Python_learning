class Settings():
    """存储所有的设置类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1280
        self.screen_height = 960
        self.bg_color = 230, 230, 230
        
        #飞船设置
        # ~ self.ship_speed_factor = 1.2
        self.ship_limit = 3
        
        #子弹设置
        # ~ self.bullet_speed_factor = 2.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255, 60, 60
        self.bullets_allowed = 3
        
        #外星人设置
        # ~ self.alien_speed_factor = 0.6 #水平移动速度
        self.fleet_drop_speed = 8 #向下移动速度
        # ~ self.fleet_direction = 1 # 1表示向右移  -1表示向左移
        
        #以什么速度加快游戏节奏
        self.speenup_scale = 1.1
        #外星人的分值倍数
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """初始化游戏设置"""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = 0.6
        self.fleet_direction = 1
        self.alien_points = 50 #击落外星人的分值
    
    def increase_speed(self):
        """提高速度设置和外星人分值"""
        self.ship_speed_factor *= self.speenup_scale
        self.bullet_speed_factor *= self.speenup_scale
        self.alien_speed_factor *= self.speenup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
