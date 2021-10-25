import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"
    MDLabel:
        text: "nick LeRA"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "автор Гмиренко Валерия"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:
        DrawerList:
            id: md_list
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Лучшее приложение созданное Лерой"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1 
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                id: content_drawer
'''

class Tab(MDFloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Valeria (MDApp):
    title = "Valeria"
    by_who = "автор Гмиренко Валерией"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item_menu_lines = {
            "account-cowboy-hat": "об авторе",
            "youtube": "My YouTube",
            "coffee": "Donate автору",
            "github": "source code",
            "share-variant": "Share app",
            "shield-sun": "Тема - Темная/Светлая",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "source code",
            "share-variant": "Chart",
            "book-open-variant": "Sum",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )
        # for name_tab in list(md_icons.keys())[15:30]:
        #     self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))

        for icon_name, name_tab in icons_item_menu_tabs.items():
            self.root.ids.tabs.add_widget(
                Tab(
                    text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[size][/font] \
                    {name_tab}"))



    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''
        Called when switching tabs.
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        # get the tab icon.
        count_icon = instance_tab.icon
        # print it on shell/bash.
        print('tab clicked!'+ tab_text)

    def on_star_click(self):
        pass

Valeria().run()
