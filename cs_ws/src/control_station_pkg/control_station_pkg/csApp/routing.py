# csApp/routing.py
from django.urls import re_path, path

from .Consumers import HDConsumer, InfoElecConsumer,NavConsumer, InfoRoverConsumer, CameraConsumer, GamepadConsumer, TimerConsumer, LogConsumer, ScienceDataConsumer, ScienceDrillConsumer
from .Consumers import SessionConsumer

websocket_urlpatterns = [
    # re_path(r'ws/csApp/(?P<tab_name>\w+)/$', NavConsumer.NavConsumer.as_asgi()),
    #path('ws/csApp/navigation/'    , NavAutoConsumer.NavAutoConsumer.as_asgi()),
    
    re_path(r'ws/cameras/(?P<v_name>\w+)/$', CameraConsumer.CameraConsumer.as_asgi()),

    path('ws/csApp/session/'        , SessionConsumer.SessionConsumer.as_asgi()),
    path('ws/csApp/log/'            , LogConsumer.LogConsumer.as_asgi()),
    path('ws/csApp/timer/'          , TimerConsumer.TimerConsumer.as_asgi()),
    path('ws/csApp/gamepad/'        , GamepadConsumer.GamepadConsumer.as_asgi()),
    path('ws/csApp/camera/'         , CameraConsumer.CameraConsumer.as_asgi()),
    
    path('ws/csApp/science_data/'  , ScienceDataConsumer.ScienceDataConsumer.as_asgi()),
    path('ws/csApp/science_drill/' , ScienceDrillConsumer.ScienceDrillConsumer.as_asgi()),

    path('ws/csApp/info_rover/'     , InfoRoverConsumer.InfoRoverConsumer.as_asgi()),
    path('ws/csApp/info_hd/'        , HDConsumer.HDConsumer.as_asgi()),
    path('ws/csApp/info_nav/'       , NavConsumer.NavConsumer.as_asgi()),

    path('ws/csApp/info_elec/'      , InfoElecConsumer.InfoElecConsumer.as_asgi()),

    #path('ws/csApp/info_science/'   , ScienceDrillConsumer.InfoScienceConsumer.as_asgi()),
    #path('ws/csApp/manual/'        , InfoNavConsumer.NavManualConsumer.as_asgi()),
    #path('ws/csApp/science/'       , ScienceDrillConsumer.ScienceDrillConsumer.as_asgi()),



    #path('ws/csApp/science/'       , ScienceDrillConsumer.ScienceDrillConsumer.as_asgi()),

]
