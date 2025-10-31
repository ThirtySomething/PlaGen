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
## Class dlgplaylistnew
###########################################################################

class dlgplaylistnew ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        m_boxsizer_playlist = wx.BoxSizer( wx.VERTICAL )

        m_boxsizer_name = wx.BoxSizer( wx.HORIZONTAL )

        self.m_statictext_name = wx.StaticText( self, wx.ID_ANY, _(u"Playlist"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        self.m_statictext_name.Wrap( -1 )

        m_boxsizer_name.Add( self.m_statictext_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textctrl_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_name.Add( self.m_textctrl_name, 0, wx.ALL, 5 )


        m_boxsizer_playlist.Add( m_boxsizer_name, 1, wx.EXPAND, 5 )

        m_boxsizer_location = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_location = wx.Button( self, wx.ID_ANY, _(u"Select location"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_location.Add( self.m_button_location, 0, wx.ALL, 5 )

        self.m_textctrl_location = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_location.Add( self.m_textctrl_location, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        m_boxsizer_playlist.Add( m_boxsizer_location, 1, wx.EXPAND, 5 )

        m_boxsizer_buttons = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_save = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_save, 0, wx.ALL, 5 )

        self.m_button_abort = wx.Button( self, wx.ID_ANY, _(u"Abort"), wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        m_boxsizer_buttons.Add( self.m_button_abort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        m_boxsizer_playlist.Add( m_boxsizer_buttons, 1, wx.EXPAND, 5 )


        self.SetSizer( m_boxsizer_playlist )
        self.Layout()
        m_boxsizer_playlist.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button_location.Bind( wx.EVT_LEFT_DOWN, self.on_btn_location )
        self.m_button_save.Bind( wx.EVT_LEFT_DOWN, self.on_btn_save )
        self.m_button_abort.Bind( wx.EVT_LEFT_DOWN, self.on_btn_abort )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_btn_location( self, event ):
        event.Skip()

    def on_btn_save( self, event ):
        event.Skip()

    def on_btn_abort( self, event ):
        event.Skip()


