# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"MyApp"), pos = wx.DefaultPosition, size = wx.Size( 589,475 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, _(u"Combo!"), wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer1.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		m_choice1Choices = ["test","test2"]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer1.Add( self.m_choice1, 0, wx.ALL, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer1.Add( self.m_listBox1, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, _(u"Check Me!"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		m_radioBox1Choices = [ _(u"Radio Button") ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, _(u"wxRadioBox"), wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer1.Add( self.m_radioBox1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.btnTest )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.cmbChanged )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTest( self, event ):
		event.Skip()

	def cmbChanged( self, event ):
		event.Skip()


