# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class frmmain
###########################################################################

class frmmain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menu_file_new = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"New playlist"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_new )

        self.m_menu_file_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Save playlist"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_save )

        self.m_menu_file_edit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Edit playlist"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_edit )

        self.m_menu_file_revert = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Revert playlist"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_revert )

        self.m_menu_file.AppendSeparator()

        self.m_menu_file_settings = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Settings"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_settings )

        self.m_menu_file.AppendSeparator()

        self.m_menu_file_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Exit"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_exit )

        self.m_menubar.Append( self.m_menu_file, _(u"File") )

        self.SetMenuBar( self.m_menubar )

        m_boxsizer_frmmain = wx.BoxSizer( wx.VERTICAL )

        m_boxsizer_playlist = wx.BoxSizer( wx.VERTICAL )

        self.m_statictext_playlist = wx.StaticText( self, wx.ID_ANY, _(u"Current playlist"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_statictext_playlist.Wrap( -1 )

        m_boxsizer_playlist.Add( self.m_statictext_playlist, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textctrl_playlist = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_textctrl_playlist.Enable( False )

        m_boxsizer_playlist.Add( self.m_textctrl_playlist, 0, wx.ALL|wx.EXPAND, 5 )


        m_boxsizer_frmmain.Add( m_boxsizer_playlist, 1, wx.EXPAND, 5 )

        m_boxsizer_drag_n_drop = wx.BoxSizer( wx.HORIZONTAL )

        self.m_statictext_drag_n_drop = wx.StaticText( self, wx.ID_ANY, _(u"Drop files/folder here"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_statictext_drag_n_drop.Wrap( -1 )

        m_boxsizer_drag_n_drop.Add( self.m_statictext_drag_n_drop, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        m_boxsizer_frmmain.Add( m_boxsizer_drag_n_drop, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_boxsizer_buttons = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_new = wx.Button( self, wx.ID_ANY, _(u"New playlist"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_new, 0, wx.ALL, 5 )

        self.m_button_save = wx.Button( self, wx.ID_ANY, _(u"Save playlist"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_save, 0, wx.ALL, 5 )

        self.m_button_edit = wx.Button( self, wx.ID_ANY, _(u"Edit playlist"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_edit, 0, wx.ALL, 5 )

        self.m_button_revert = wx.Button( self, wx.ID_ANY, _(u"Revert changes"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_revert, 0, wx.ALL, 5 )


        m_boxsizer_frmmain.Add( m_boxsizer_buttons, 1, wx.EXPAND, 5 )


        self.SetSizer( m_boxsizer_frmmain )
        self.Layout()
        m_boxsizer_frmmain.Fit( self )
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_app_close )
        self.Bind( wx.EVT_MENU, self.on_menu_file_new, id = self.m_menu_file_new.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_save, id = self.m_menu_file_save.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_edit, id = self.m_menu_file_edit.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_revert, id = self.m_menu_file_revert.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_settings, id = self.m_menu_file_settings.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_exit, id = self.m_menu_file_exit.GetId() )
        self.m_button_new.Bind( wx.EVT_LEFT_DOWN, self.on_btn_playlist_new )
        self.m_button_save.Bind( wx.EVT_LEFT_DOWN, self.on_btn_playlist_save )
        self.m_button_edit.Bind( wx.EVT_LEFT_DOWN, self.on_btn_playlist_edit )
        self.m_button_revert.Bind( wx.EVT_LEFT_DOWN, self.on_btn_playlist_revert )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_app_close( self, event ):
        event.Skip()

    def on_menu_file_new( self, event ):
        event.Skip()

    def on_menu_file_save( self, event ):
        event.Skip()

    def on_menu_file_edit( self, event ):
        event.Skip()

    def on_menu_file_revert( self, event ):
        event.Skip()

    def on_menu_file_settings( self, event ):
        event.Skip()

    def on_menu_file_exit( self, event ):
        event.Skip()

    def on_btn_playlist_new( self, event ):
        event.Skip()

    def on_btn_playlist_save( self, event ):
        event.Skip()

    def on_btn_playlist_edit( self, event ):
        event.Skip()

    def on_btn_playlist_revert( self, event ):
        event.Skip()


