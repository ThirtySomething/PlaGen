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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menu_file_new = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"New playlist"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_new )

        self.m_menu_file.AppendSeparator()

        self.m_menu_file_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"Exit"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menu_file_exit )

        self.m_menubar.Append( self.m_menu_file, _(u"File") )

        self.SetMenuBar( self.m_menubar )

        m_boxsizer_frmmain = wx.BoxSizer( wx.VERTICAL )

        m_boxsizer_playlist = wx.BoxSizer( wx.HORIZONTAL )


        m_boxsizer_frmmain.Add( m_boxsizer_playlist, 1, wx.EXPAND, 5 )


        self.SetSizer( m_boxsizer_frmmain )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_app_close )
        self.Bind( wx.EVT_MENU, self.on_menu_file_new, id = self.m_menu_file_new.GetId() )
        self.Bind( wx.EVT_MENU, self.on_menu_file_exit, id = self.m_menu_file_exit.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_app_close( self, event ):
        event.Skip()

    def on_menu_file_new( self, event ):
        event.Skip()

    def on_menu_file_exit( self, event ):
        event.Skip()


