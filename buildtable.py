#!/usr/bin/env python
import os
import pprint
import json
import re

featureMatrix = {
    'accessibility' : { # Checked
        'Accessibility':dict(),
        'AccessibilityImplementation':dict(),
        'AccessibilityProperties': dict(),
        'ISearchableText': dict(),
        'ISimpleTextSelection': dict()
    },
    #'automation' : { # Checked
    #    'ActionGenerator': dict(),
    #    'AutomationAction':dict(),
    #    'Configuration':dict(),
    #    'KeyboardAutomationAction':dict(),
    #    'MouseAutomationAction':dict(),
    #    'StageCapture':dict(),
    #    'StageCaptureEvent':dict()
    #},
    'desktop' : { # Checked
        'Clipboard':dict(),
        'ClipboardFormats':dict(),
        'ClipboardTransferMode':dict(),
        'IFilePromise':dict()
     	#Icon AIR
     	#InteractiveIcon AIR
     	#InvokeEventReason AIR
     	#NativeApplication AIR
     	#NativeDragActions AIR
     	#NativeDragManager AIR
     	#NativeDragOptions AIR
     	#NativeProcess AIR
     	#NativeProcessStartupInfo AIR
     	#NotificationType AIR
     	#SystemIdleMode AIR
     	#SystemTrayIcon AIR
     	#Updater AIR
    },
    'display' : { # Checked
        'AVM1Movie': dict(),
        'ActionScriptVersion': dict(),
        'AVM1Movie': dict(),
        'Bitmap': dict(),
        'BitmapData': dict(),
        'BitmapDataChannel': dict(),
        'BitmapEncodingColorSpace': dict(),
        'BlendMode': dict(),
        'CapsStyle': dict(),
        'ColorCorrection': dict(),
        'ColorCorrectionSupport': dict(),
        'DisplayObject': dict(),
        'DisplayObjectContainer': dict(),
        #'FocusDirection': dict(), Is AIR
        'FrameLabel': dict(),
        'GradientType': dict(),
        'Graphics': dict(),
        'GraphicsBitmapFill': dict(),
        'GraphicsEndFill': dict(),
        'GraphicsGradientFill': dict(),
        'GraphicsPath': dict(),
        'GraphicsPathCommand': dict(),
        'GraphicsPathWinding': dict(),
        'GraphicsShaderFill': dict(),
        'GraphicsSolidFill': dict(),
        'GraphicsStroke': dict(),
        'GraphicsTrianglePath': dict(),
        'IBitmapDrawable': dict(),
        'IDrawCommand': dict(),
        'IGraphicsData': dict(),
        'IGraphicsFill': dict(),
        'IGraphicsPath': dict(),
        'IGraphicsStroke': dict(),
        'InteractiveObject': dict(),
        'InterpolationMethod': dict(),
        'JointStyle': dict(),
        'JPEGEncoderOptions': dict(),
        'JPEGXREncoderOptions': dict(),
        'LineScaleMode': dict(),
        'Loader': dict(),
        'LoaderInfo': dict(),
        'MorphShape': dict(),
        'MovieClip': dict(),
        'MovieClipSoundStream': dict(),
        #'NativeMenu': dict(),
     	#'NativeMenuItem': dict(),
     	#'NativeWindow': dict(),
     	#'NativeWindowDisplayState': dict(),
     	#'NativeWindowInitOptions': dict(),
     	#'NativeWindowRenderMode': dict(),
     	#'NativeWindowResize': dict(),
     	#'NativeWindowSystemChrome': dict(),
     	#'NativeWindowType': dict(),
        'PixelSnapping': dict(),
        'PNGEncoderOptions': dict(),
        'Scene': dict(),
        #Screen
        #ScreenMode
        'Shader': dict(),
        'ShaderData': dict(),
        'ShaderInput': dict(),
        'ShaderJob': dict(),
        'ShaderParameter': dict(),
        'ShaderParameterType': dict(),
        'ShaderPrecision': dict(),
        'Shape': dict(),
        'SimpleButton': dict(),
        'SpreadMethod': dict(),
        'Sprite': dict(),
        'Stage': dict(),
        'Stage3D': dict(),
        'StageAlign': dict(),
        #	StageAspectRatio    
        'StageDisplayState': dict(),
        #StageOrientation
        'StageQuality': dict(),
        'StageScaleMode': dict(),
        'SWFVersion': dict(),
        'TriangleCulling': dict()
    },
    'display3D' : { # Checked
        'Context3D': dict(),
        'Context3DBlendFactor': dict(),
        'Context3DBufferUsage': dict(),
        'Context3DClearMask': dict(),
        'Context3DCompareMode': dict(),
        #Context3DFillMode   AIR
        'Context3DMipFilter': dict(),
        'Context3DProfile': dict(),
        'Context3DProgramType': dict(),
        'Context3DRenderMode': dict(),
        'Context3DStencilAction': dict(),
        'Context3DTextureFilter': dict(),
        'Context3DTextureFormat': dict(),
        'Context3DTriangleFace': dict(),
        'Context3DVertexBufferFormat': dict(),
        'Context3DWrapMode': dict(),
        'IndexBuffer3D': dict(),
        'Program3D': dict(),
        'VertexBuffer3D': dict(),
    },
    'errors' : {
        #'DRMManagerError': dict(), AIR
        'EOFError': dict(),
        'IllegalOperationError': dict(),
        'InvalidSWFError': dict(),
        'IOError': dict(),
        'MemoryError': dict(),
        # 'PermissionError': dict(), AIR
        'ScriptTimeoutError': dict(),
        #'SQLError': dict(), AIR
        #'SQLErrorOperation': dict(), AIR
        'StackOverflowError': dict()
    },
    'events' : {
        'AccelerometerEvent': dict(),
        'ActivityEvent': dict(),
        'AsyncErrorEvent': dict(),
        # BrowserInvokeEvent AIR
        'ContextMenuEvent': dict(),
        'DataEvent': dict(),
        'ErrorEvent': dict(),
        'Event': dict(),
        'EventDispatcher': dict(),
        'EventPhase': dict(),
        'FocusEvent': dict(),
        'FullScreenEvent': dict(),
        'GameInputEvent': dict(),
        'GeolocationEvent': dict(),
        'GestureEvent': dict(),
        'IDrawCommand': dict(),
        'GesturePhase': dict(),
        'IGraphicsData': dict(),
        'IGraphicsFill': dict(),
        'HTTPStatusEvent': dict(),
        'IGraphicsPath': dict(),
        'IGraphicsStroke': dict(),
        'IEventDispatcher': dict(),
        'InteractiveObject': dict(),
        'InterpolationMethod': dict(),
        'IMEEvent': dict(),
        'JointStyle': dict(),
        'JPEGEncoderOptions': dict(),
        'IOErrorEvent': dict(),
        'LineScaleMode': dict(),
        'KeyboardEvent': dict(),
        'Loader': dict(),
        'LoaderInfo': dict(),
        'MouseEvent': dict(),
        'MorphShape': dict(),
        'MovieClip': dict(),
        'NetDataEvent': dict(),
        'NetFilterEvent': dict(),
        'NetMonitorEvent': dict(),
        'NetStatusEvent': dict(),
        'OutputProgressEvent': dict(),
        'PressAndTapGestureEvent': dict(),
        'ProgressEvent': dict(),
        'SampleDataEvent': dict(),
        'SecurityErrorEvent': dict(),
        'ShaderEvent': dict(),
        'SoftKeyboardEvent': dict(),
        'SoftKeyboardTrigger': dict(),
        'StageVideoAvailabilityEvent': dict(),
        'StageVideoEvent': dict(),
        'StatusEvent': dict(),
        'SyncEvent': dict(),
        'TextEvent': dict(),
        'ThrottleEvent': dict(),
        'ThrottleType': dict(),
        'TimerEvent': dict(),
        'TouchEvent': dict(),
        'TransformGestureEvent': dict(),
        'UncaughtErrorEvent': dict(),
        'UncaughtErrorEvents': dict(),
        'VideoEvent': dict()
    },
    'external' : { # Checked
        # 'ExtensionContext' AIR
        'ExternalInterface':dict()
    },
    'filters' : { # Checked
        'BevelFilter': dict(),
        'BevelFilter': dict(),
        'BitmapFilter': dict(),
        'BitmapFilterQuality': dict(),
        'BitmapFilterType': dict(),
        'BlurFilter': dict(),
        'ColorMatrixFilter': dict(),
        'ConvolutionFilter': dict(),
        'DisplacementMapFilter': dict(),
        'DisplacementMapFilterMode': dict(),
        'DropShadowFilter': dict(),
        'GlowFilter': dict(),
        'GradientBevelFilter': dict(),
        'GradientGlowFilter': dict(),
        'ShaderFilter': dict()
    },
    'geom' : { # Checked
        'ColorTransform': dict(),
        'Matrix': dict(),
        'Matrix3D': dict(),
        'Orientation3D': dict(),
        'PerspectiveProjection': dict(),
        'Point': dict(),
        'Rectangle': dict(),
        'Transform': dict(),
        'Utils3D': dict(),
        'Vector3D': dict()
    },
    'globalization' : { # Checked
        'Collator': dict(),
        'CollatorMode': dict(),
        'CurrencyFormatter': dict(),
        'CurrencyParseResult': dict(),
        'DateTimeFormatter': dict(),
        'DateTimeNameContext': dict(),
        'DateTimeNameStyle': dict(),
        'DateTimeStyle': dict(),
        'LastOperationStatus': dict(),
        'LocaleID': dict(),
        'NationalDigitsType': dict(),
        'NumberFormatter': dict(),
        'NumberParseResult': dict(),
        'StringTools': dict()
    },
    'media' : { # Checked
        'AudioDecoder': dict(),
        'AudioDeviceManager': dict(),
        'AudioOutputChangeReason': dict(),
        #AudioPlaybackMode AIR
        'AVNetworkingParams': dict(),
        'AVTagData': dict(),
        'AVURLLoader': dict(),
        'AVURLStream': dict(),
        'Camera': dict(),
        #CameraPositionAIR
        #CameraRollAIR
        #CameraRollBrowseOptionsAIR
        #CameraUIAIR
        'H264Level': dict(),
        'H264Profile': dict(),
        'H264VideoStreamSettings': dict(),
        'ID3Info': dict(),
        #MediaPromise AIR
        #MediaType AIR
        'Microphone': dict(),
        'MicrophoneEnhancedMode': dict(),
        'MicrophoneEnhancedOptions': dict(),
        'Sound': dict(),
        'SoundChannel': dict(),
        'SoundCodec': dict(),
        'SoundLoaderContext': dict(),
        'SoundMixer': dict(),
        'SoundTransform': dict(),
        'StageVideo': dict(),
        'StageVideoAvailability': dict(),
        'StageVideoAvailabilityReason': dict(),
        #StageWebView AIR
        'Video': dict(),
        'VideoCodec': dict(),
        'VideoStatus': dict(),
        'VideoStreamSettings': dict()
    },
    'net' : { # Checked
        'DatagramSocket': dict(),
        'FileFilter': dict(),
        'FileReference': dict(),
        'FileReferenceList': dict(),
        'GroupSpecifier': dict(),
        #'InterfaceAddress': dict(), AIR
        #'IPVersion': dict(), AIR
        'LocalConnection': dict(),
        'NetConnection': dict(),
        'NetGroup': dict(),
        'NetGroupInfo': dict(),
        'NetGroupReceiveMode': dict(),
        'NetGroupReplicationStrategy': dict(),
        'NetGroupSendMode': dict(),
        'NetGroupSendResult': dict(),
        'NetMonitor': dict(),
        'NetStream': dict(),
        'NetStreamAppendBytesAction': dict(),
        'NetStreamInfo': dict(),
        'NetStreamMulticastInfo': dict(),
        'NetStreamPlayOptions': dict(),
        'NetStreamPlayTransitions': dict(),
        #'NetworkInfo': dict(), AIR
        #'NetworkInterface': dict(), AIR
        'ObjectEncoding': dict(),
        'Responder': dict(),
        'SecureSocket': dict(),
        #'ServerSocket': dict(), AIR
        'SharedObject': dict(),
        'SharedObjectFlushStatus': dict(),
        'Socket': dict(),
        'URLLoader': dict(),
        'URLLoaderDataFormat': dict(),
        'URLRequest': dict(),
        'URLRequestDefaults': dict(),
        'URLRequestHeader': dict(),
        'URLRequestMethod': dict(),
        'URLStream': dict(),
        'URLVariables': dict(),
        'XMLSocket': dict()
    },
    'printing' : { # Checked
        #'PaperSize': dict(), AIR
        'PrintJob': dict(),
        'PrintJobOptions': dict(),
        'PrintJobOrientation': dict(),
        # 'PrintMethod': dict(), AIR
        #'PrintUIOptions': dict(), AIR
    },
    'profiler' : { # Checked
        'Telemetry': dict()
    },
    'sampler' : { # Checked
        'DeleteObjectSample': dict(),
        'NewObjectSample': dict(),
        'Sample': dict(),
        'StackFrame': dict()
    },
    'security' : { # Checked
        'CertificateStatus': dict(),
        #'ReferencesValidationSetting': dict(),
        #'RevocationCheckSettings': dict(),
        #'SignatureStatus': dict(),
        #'SignerTrustSettings': dict(),
        #'X500DistinguishedName': dict(),
        'X509Certificate': dict(),
        #'XMLSignatureValidator': dict(),
    },
    'sensors' : { # Checked
        'Accelerometer': dict(),
        #'DeviceRotation': dist(), AIR
        #'Geolocation': dict(), AIR
    },
    'system' : { # Checked
        'ApplicationDomain': dict(),
        'Capabilities': dict(),
        #'ImageDecodingPolicy': dict(), AIR
        'IME': dict(),
        'IMEConversionMode': dict(),
        'JPEGLoaderContext': dict(),
        'LoaderContext': dict(),
        'MessageChannel': dict(),
        'MessageChannelState': dict(),
        'Security': dict(),
        'SecurityDomain': dict(),
        'SecurityPanel': dict(),
        'System': dict(),
        'SystemUpdater': dict(),
        'SystemUpdaterType': dict(),
        'TouchscreenType': dict(),
        'Worker': dict(),
        'WorkerDomain': dict(),
        'WorkerState': dict(),
    },
    'text' : { # Checked
        'AntiAliasType': dict(),
        #'AutoCapitalize' AIR
        'CSMSettings': dict(),
        'Font': dict(),
        'FontStyle': dict(),
        'FontType': dict(),
        'GridFitType': dict(),
        #ReturnKeyLabel AIR
    	#SoftKeyboardType AIR
    	#StageText AIR
     	#StageTextClearButtonMode AIR
     	#StageTextInitOptions AIR
        'StaticText': dict(),
        'StyleSheet': dict(),
        'TextColorType': dict(),
        'TextDisplayMode': dict(),
        'TextField': dict(),
        'TextFieldAutoSize': dict(),
        'TextFieldType': dict(),
        'TextFormat': dict(),
        'TextFormatAlign': dict(),
        #'TextFormatDisplay': dict(),
        'TextInteractionMode': dict(),
        'TextLineMetrics': dict(),
        'TextRenderer': dict(),
        'TextSnapshot': dict(),
    },
    'trace' : {
        'Trace': dict()
    },
    'ui' : { # Checked
        'ContextMenu': dict(),
        'ContextMenuBuiltInItems': dict(),
        'ContextMenuClipboardItems': dict(),
        'ContextMenuItem': dict(),
        #'GameInput': dict(), AIR
        #'GameInputControl': dict(), AIR
        #'GameInputDevice': dict(), AIR
        #'GameInputFinger': dict(),
        #'GameInputHand': dict(),
        'KeyLocation': dict(),
        'Keyboard': dict(),
        'KeyboardType': dict(),
        'Mouse': dict(),
        'MouseCursor': dict(),
        'MouseCursorData': dict(),
        'Multitouch': dict(),
        'MultitouchInputMode': dict()
    },
    'utils' : { # Checked
        'CompressionAlgorithm': dict(),
        'Endian': dict(),
        'IDataInput': dict(),
        'IDataOutput': dict(),
        'Timer': dict(),
        'ByteArray': dict(),
        'Dictionary': dict()
    }
}

# Add Flash Players
for category in featureMatrix:
    for feature in featureMatrix[category]:
        featureMatrix[category][feature] = {'adobeflash' : 'Yes', 'shumway' : 'No', 'lightspark': 'No', 'gnash': 'No'}

#def getShumwayFiles():
#    shumwayFeatures = []
#    dir = './shumway/src/flash'
#    for subdir, dirs, files in os.walk(dir):
#        for file in files:
#            if file.endswith(".ts"):
#                filePath = (os.path.join(subdir, file))
#                shumwayFeatures.append(filePath)
#    return shumwayFeatures
#
#
#def getLightsparkFiles():
#    dir = './lightspark/src/scripting/flash'
#    lightsparkFeatures = []
#    for subdir, dirs, files in os.walk(dir):
#        for file in files:
#            if file.endswith(".cpp"):
#                filePath = (os.path.join(subdir, file))
#                lightsparkFeatures.append(filePath)
#    return lightsparkFeatures
#
#def getGnashFiles():
#    gnashFeatures = []
#    dir = './gnash/tree/master/libcore/asobj'
#    for subdir, dirs, files in os.walk(dir):
#        for file in files:
#            if file.endswith(".ts"):
#                filePath = (os.path.join(subdir, file))
#                gnashFeatures.append(filePath)
#    return gnashFeatures







# Parse files

dir = './shumway/src/flash'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.ts'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            subDirKey = subdir.replace(dir + '/','')
            fileKey = file.replace('.ts', '')
            if subDirKey in featureMatrix.keys():
                if fileKey in featureMatrix[subDirKey].keys():
                    if lines.find('notImplemented(') > 0:
                        featureMatrix[subDirKey][fileKey]['shumway'] = 'No' # No
                    elif lines.find('somewhatImplemented(') > 0:
                        featureMatrix[subDirKey][fileKey]['shumway'] = 'Partially'
                    else:
                        featureMatrix[subDirKey][fileKey]['shumway'] = 'Yes'

# Use https://github.com/mozilla/shumway/blob/16451d8836fa85f4b16eeda8b4bda2fa9e2b22b0/utils/playerglobal-builder/manifest.json
# for better understanding of what is supported.








dir = './gnash/libcore/asobj/'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('_as.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            subDirKey = subdir.replace(dir + '/','')
            fileKey = file.replace('_as.cpp', '')
            for item in featureMatrix:
                if fileKey in featureMatrix[item].keys():
                    featureMatrix[item][fileKey]['gnash'] = 'Yes'

for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            m = re.findall('\w+\(vm, "(\w+)"\)', lines)     # Be more specific
            for item in featureMatrix:
                for found in m:
                    if fileKey in featureMatrix[item].keys():
                        featureMatrix[item][fileKey]['gnash'] = 'Yes'

# Find Lightspark features
fileContent = open('./lightspark/src/scripting/abc.cpp', "r")
lines = fileContent.read()
m = re.findall('builtin\-\>registerBuiltin\("(\w+)",', lines)
for item in featureMatrix:
    for found in m:
        if found in featureMatrix[item].keys():
            featureMatrix[item][found]['lightspark'] = 'Yes'

# Find more lightspark features - This needs to be improved
fileContent = open('./lightspark/src/allclasses.h', "r")
lines = fileContent.read()
m = re.findall('REGISTER_CLASS_NAME\((\w+),\"(.*)\"', lines)
# Fill in matrix here TODO

m = re.findall('REGISTER_CLASS_NAME2\((\w+),\"(.*)\"', lines)
# Fill in matrix here TODO


# Find "Not implemented in all features to set as partially complete"
dir = './lightspark/src/scripting/'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            m = re.findall('LOG\(LOG_NOT_IMPLEMENTED,\"(\w+) is not implemented', lines)
            for item in featureMatrix:
                for found in m:
                    if found in featureMatrix[item].keys():
                        featureMatrix[item][found]['lightspark'] = 'Partially' # No

# Find "Not implemented in all features to set as partially complete"
dir = './lightspark/src/scripting/'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            m = re.findall('LOG\(LOG_NOT_IMPLEMENTED,\"(\w+)\.', lines)
            for item in featureMatrix:
                for found in m:
                    if found in featureMatrix[item].keys():
                        featureMatrix[item][found]['lightspark'] = 'Partially'


featureMatrix['trace']['Trace']['lightspark'] = 'Yes'


#Override features
featureMatrix['display']['Shader']['lightspark'] = 'No'
featureMatrix['display']['Shader']['shumway'] = 'No'
featureMatrix['display']['ShaderInput']['shumway'] = 'No'
featureMatrix['display']['ShaderJob']['shumway'] = 'No'
featureMatrix['display']['ShaderParameter']['shumway'] = 'No'
featureMatrix['display']['ShaderPrecision']['shumway'] = 'No'


with open("flash-matrix.json", "w") as write_file:
    json.dump(featureMatrix, write_file)
