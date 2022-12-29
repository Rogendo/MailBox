SPLASHSCREEN='''
MDScreen:
    name:"splash"
    
    MDFloatLayout:
        md_bg_color:"blue"
        MDLabel:
            text:"MAIL BOX"
            halign:"center"


'''


KV = '''
#Colors

<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

# Colors End 

<ContentNavigationDrawer>

    MDNavigationDrawerMenu:

        MDNavigationDrawerHeader:
            title: "MailBox"
            title_color: "#4a4939"
            text: ""
            spacing: "4dp"
            padding: "12dp", 0, 0, "56dp"

        MDNavigationDrawerLabel:
            text: "Mail"
            title_color: "#4a4939"

        DrawerClickableItem:
            icon: "gmail"
            right_text: "+99"
            text_right_color: "#4a4939"
            text: "Inbox"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "inbox"
        DrawerClickableItem:
            icon: "send"
            text: "Outbox"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "outbox"

        DrawerClickableItem:
            icon:"file"
            text:"Draft"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current="draft"

        DrawerClickableItem:
            icon:"information-outline"
            text:"Spam"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current="spam"

        DrawerClickableItem:
            icon:"trash-can"
            text:"Trash"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current="trash"

        MDNavigationDrawerDivider:

        MDNavigationDrawerLabel:
            text: "..."


        DrawerClickableItem:
            icon: "tools"
            text: "Settings"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current="settings"

        DrawerClickableItem:
            icon: "help-rhombus"
            text: "Help & Feedback"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current="help"

        MDNavigationDrawerDivider:

        #MDNavigationDrawerLabel:
            # text: "version 1.0.0"


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        # MDTextField:
        #     hint_text: "Search"
        #     mode: "round"
        #     height: "30dp"
        #     width:"10dp"


    MDNavigationLayout:


        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "inbox"

                MDLabel:
                    text: "Inbox Screen"
                    halign: "center"
                
                MDCard:
                    orientation:"vertical"
                    size_hint:None,None
                    size:"340dp","560dp"
                    pos_hint:{"center_x":.5,"center_y":.45}
                    md_bg_color:"grey"
                    
                    # MDLabel:
                    #     text:"Inbox"
                    #     # halign:"left"
                    #     pos_hint:{"center_x":.5,"center_y":.5}
                    #     
                    OneLineAvatarIconListItem:
                        text:"Quora Digest"
                        on_release:print("clicked")
                        
                        IconLeftWidget:
                            icon:"information"
                            
                    MDSeparator:
                        height:"1dp"
                        
                    OneLineAvatarIconListItem:
                        text:"Udacity"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"book-education"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Kabarak University"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"school"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Dr. Moses"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"account"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Peter Snow"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"account"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Udacity"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"book-education"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Udacity"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"book-education"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Udacity"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"book-education"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"Cole Nickson"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"account"
                    MDSeparator:
                        height:"1dp"
                    OneLineAvatarIconListItem:
                        text:"James Underson"
                        on_release:print("clicked")
                        IconLeftWidget:
                            icon:"account"
                    MDSeparator:
                        height:"1dp"
                  
                    

                MDFloatingActionButton:
                    icon: "pen"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint:{"center_x":.9,"center_y":0.06}
                    on_press:
                        root.screen_manager.current('new')



            MDScreen:
                name: "outbox"

                MDLabel:
                    text: "Nothing in OutBox "
                    pos_hint:{"center_x":.5,"center_y":.4}
                    halign:"center"
                    
                MDIcon:
                    icon:"code-not-equal"
                    font_size:"80dp"
                    pos_hint:{"center_x":.5,"center_y":.5}
            MDScreen:
                name: "draft"

                MDLabel:
                    text: "Drafts Screen"
                    halign: "center"

            MDScreen:
                name:"spam"

                MDLabel:
                    text:"No spam mail"
                    halign:"center"

            MDScreen:
                name:"trash"
                MDIcon:
                    icon:'trash-can-outline'
                    font_size:"80"
                    pos_hint:{"center_x":.5,"center_y":.6}

                MDLabel:
                    text:"Trash is empty"
                    halign:"center"
                    

            MDScreen:
                name:"settings"

                MDSwitch:

                    widget_style: "android"
                    pos_hint:{"center_x":.1,"center_y":0.85}
                    on_active:app.switch_theme_style()

                    thumb_color:0,0,0
                    theme_thumb_down_color:0,0,255
                    # switch_animation: True
                    # app.switch_theme_style()
                    # width:dp(30)
                    active:True
                    
               
                MDLabel:
                    text:"Dark theme"
                    halign:"right"

            MDScreen:
                name:"help"


                MDCard:
                    orientation:"vertical"
                    size_hint:None,None
                    size:"280dp","300dp"
                    pos_hint:{"center_x":.5,"center_y":.6}
                    md_bg_color:"grey"
                    # ripple_behavior:True

                    MDLabel:
                        text:"FAQs"
                        halign:"center"
                        text_color:"white"
                        height:self.texture_size[1]
                        bold:True
                        underline:True
                    MDSeparator:
                        height:"0.5dp"



                    OneLineAvatarIconListItem:
                        text:"Sign in to MailBox"
                        on_release:print("clicked")

                        IconLeftWidget:
                            icon:"account"
                    OneLineAvatarIconListItem:
                        text:"Create Mailbox account"
                        on_release:print("clicked")

                        IconLeftWidget:
                            icon:"account"

                    OneLineAvatarIconListItem:
                        text:"Your Mailbox Settings"
                        on_release:print("clicked")

                        IconLeftWidget:
                            icon:"tools"

                    OneLineAvatarIconListItem
                        text:"Send Feedback in Mailbox"
                        on_release:print("clicked")

                        IconLeftWidget:
                            icon:"information"



            MDScreen:
                name:'new'
                # MDLabel:
                #     text:"Compose new mail"
                #     halign:"center"
                MDTextField:
                    hint_text:"From"
                    helper_text: "user@gmail.com"
                    validator: "email"
                    halign:"left"
                    valign:"top"
                # MDTextField:
                #     hint_text:"To"
                #     helper_text: "user@gmail.com"
                #     validator: "email"
                # MDTextField:
                #     text:"Subject"
                # MDTextField:
                #     hint_text:"Compose"
                #     multiline:True
                #     mode:fill


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
