object Form1: TForm1
  Left = 0
  Top = 0
  AutoSize = True
  Caption = 'VK POST Client by Rulenko P-41'
  ClientHeight = 626
  ClientWidth = 601
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label2: TLabel
    Left = 24
    Top = 56
    Width = 41
    Height = 13
    Caption = #1055#1072#1088#1086#1083#1100':'
  end
  object Label3: TLabel
    Left = 144
    Top = 541
    Width = 55
    Height = 13
    Caption = 'ID '#1075#1088#1091#1087#1087#1099':'
    Visible = False
  end
  object Label4: TLabel
    Left = 299
    Top = 272
    Width = 104
    Height = 13
    Caption = #1055#1088#1080#1082#1088#1077#1087#1080#1090#1100' '#1089#1089#1099#1083#1082#1091':'
  end
  object Label5: TLabel
    Left = 296
    Top = 0
    Width = 104
    Height = 13
    Caption = #1056#1072#1073#1086#1090#1072#1077#1084' '#1089' '#1075#1088#1091#1087#1087#1086#1081':'
  end
  object Label6: TLabel
    Left = 16
    Top = 181
    Width = 128
    Height = 13
    Caption = #1057#1090#1072#1090#1080#1089#1090#1080#1082#1072' '#1089#1086#1086#1073#1097#1077#1089#1090#1074#1072':'
  end
  object GroupBox1: TGroupBox
    Left = 0
    Top = 0
    Width = 281
    Height = 169
    Caption = #1040#1074#1090#1086#1088#1080#1079#1072#1094#1080#1103
    TabOrder = 0
    object Label1: TLabel
      Left = 24
      Top = 27
      Width = 34
      Height = 13
      Caption = #1051#1086#1075#1080#1085':'
    end
    object LoginEdit: TEdit
      Left = 80
      Top = 24
      Width = 177
      Height = 21
      TabOrder = 0
    end
    object PassEdit: TEdit
      Left = 80
      Top = 51
      Width = 177
      Height = 21
      PasswordChar = '*'
      TabOrder = 1
    end
    object Button1: TButton
      Left = 24
      Top = 88
      Width = 233
      Height = 25
      Caption = #1040#1074#1090#1086#1088#1080#1079#1072#1094#1080#1103
      TabOrder = 2
      OnClick = Button1Click
    end
    object btnInfo: TButton
      Left = 192
      Top = 128
      Width = 65
      Height = 25
      Caption = #1057#1087#1088#1072#1074#1082#1072
      TabOrder = 3
      OnClick = btnInfoClick
    end
  end
  object GroupBox2: TGroupBox
    Left = 296
    Top = 51
    Width = 305
    Height = 212
    Caption = #1057#1086#1086#1073#1097#1077#1085#1080#1077
    TabOrder = 1
    object MessageMemo: TMemo
      Left = 11
      Top = 16
      Width = 281
      Height = 185
      TabOrder = 0
    end
  end
  object GroupEdit: TEdit
    Left = 216
    Top = 538
    Width = 204
    Height = 21
    TabOrder = 2
    Visible = False
  end
  object AttachEdit: TEdit
    Left = 409
    Top = 269
    Width = 179
    Height = 21
    TabOrder = 3
  end
  object GroupBox3: TGroupBox
    Left = 0
    Top = 344
    Width = 601
    Height = 282
    Caption = #1051#1086#1075':'
    TabOrder = 4
    object LogMemo: TMemo
      Left = 13
      Top = 16
      Width = 575
      Height = 249
      TabOrder = 0
    end
  end
  object StartButton: TButton
    Left = 296
    Top = 296
    Width = 292
    Height = 33
    Caption = #1054#1087#1091#1073#1083#1080#1082#1086#1074#1072#1090#1100
    TabOrder = 5
    OnClick = StartButtonClick
  end
  object cmbGroups: TComboBox
    Left = 307
    Top = 24
    Width = 281
    Height = 21
    BiDiMode = bdLeftToRight
    ParentBiDiMode = False
    TabOrder = 6
    Text = #1057#1087#1080#1089#1086#1082' '#1074#1072#1096#1080#1093' '#1075#1088#1091#1087#1087
    OnClick = cmbGroupsClick
  end
  object lstStat: TListBox
    Left = 16
    Top = 200
    Width = 265
    Height = 129
    ItemHeight = 13
    TabOrder = 7
  end
  object Timer1: TTimer
    Enabled = False
    Interval = 60000
    OnTimer = Timer1Timer
    Left = 24
    Top = 136
  end
  object IdHTTP1: TIdHTTP
    IOHandler = IdSSLIOHandlerSocketOpenSSL1
    AllowCookies = True
    HandleRedirects = True
    ProxyParams.BasicAuthentication = False
    ProxyParams.ProxyPort = 0
    Request.ContentLength = -1
    Request.ContentRangeEnd = -1
    Request.ContentRangeStart = -1
    Request.ContentRangeInstanceLength = -1
    Request.Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    Request.BasicAuthentication = False
    Request.UserAgent = 'Mozilla/3.0 (compatible; Indy Library)'
    Request.Ranges.Units = 'bytes'
    Request.Ranges = <>
    HTTPOptions = [hoForceEncodeParams]
    Left = 56
    Top = 136
  end
  object IdSSLIOHandlerSocketOpenSSL1: TIdSSLIOHandlerSocketOpenSSL
    MaxLineAction = maException
    Port = 0
    DefaultPort = 0
    SSLOptions.Mode = sslmUnassigned
    SSLOptions.VerifyMode = []
    SSLOptions.VerifyDepth = 0
    Left = 88
    Top = 136
  end
end