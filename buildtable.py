#!/usr/bin/env python
import os
import pprint
import json
import re

featureMatrix = {
    'accessibility' : {'Accessibility':dict(),'AccessibilityImplementation':dict(), 'AccessibilityProperties': dict(), 'ISearchableText': dict(), 'ISimpleTextSelection': dict()},
    'automation' : {'ActionGenerator': dict(), 'AutomationAction':dict(), 'Configuration':dict(), 'KeyboardAutomationAction':dict(), 'MouseAutomationAction':dict(), 'StageCapture':dict(), 'StageCaptureEvent':dict()},
    'desktop' : {'Clipboard':dict(), 'ClipboardFormats':dict(), 'ClipboardTransferMode':dict()},
    'display' : {
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
        'FocusDirection': dict(),
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
        'NativeMenu': dict(),
        'NativeMenuItem': dict(),
        'PixelSnapping': dict(),
        'PNGEncoderOptions': dict(),
        'Scene': dict(),
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
        'StageDisplayState': dict(),
        'StageQuality': dict(),
        'StageScaleMode': dict(),
        'SWFVersion': dict(),
        'TriangleCulling': dict()
    },
    'display3D' : {
        'Context3D': dict(),
        'Context3DBlendFactor': dict(),
        'Bitmap': dict(),
        'BitmapData': dict(),
        'Context3DClearMask': dict(),
        'BitmapDataChannel': dict(),
        'BitmapEncodingColorSpace': dict(),
        'Context3DCompareMode': dict(),
        'BlendMode': dict(),
        'CapsStyle': dict(),
        'Context3DProfile': dict(),
        'ColorCorrection': dict(),
        'ColorCorrectionSupport': dict(),
        'Context3DProgramType': dict(),
        'DisplayObject': dict(),
        'DisplayObjectContainer': dict(),
        'Context3DRenderMode': dict(),
        'FocusDirection': dict(),
        'FrameLabel': dict(),
        'Context3DStencilAction': dict(),
        'GradientType': dict(),
        'Graphics': dict(),
        'Context3DTextureFormat': dict(),
        'GraphicsBitmapFill': dict(),
        'GraphicsEndFill': dict(),
        'Context3DTriangleFace': dict(),
        'GraphicsGradientFill': dict(),
        'GraphicsPath': dict(),
        'Context3DVertexBufferFormat': dict(),
        'GraphicsPathCommand': dict(),
        'GraphicsPathWinding': dict(),
        'IndexBuffer3D': dict(),
        'GraphicsShaderFill': dict(),
        'GraphicsSolidFill': dict(),
        'Program3D': dict(),
        'GraphicsStroke': dict(),
        'GraphicsTrianglePath': dict(),
        'VertexBuffer3D': dict(),
        'IBitmapDrawable': dict()
    },
    'errors' : {
        'InvalidSWFError': dict(),
        'MemoryError': dict(),
        'ScriptTimeoutError': dict(),
        'StackOverflowError': dict(),
        'IllegalOperationError': dict(),
        'EOFError': dict(),
        'IOError': dict()
    },
    'events' : {
        'AccelerometerEvent': dict(),
        'ActivityEvent': dict(),
        'AsyncErrorEvent': dict(),
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
        'JPEGXREncoderOptions': dict(),
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
    'external' : {
        'ExternalInterface':dict()
    },
    'filters' : {
        'BevelFilter': dict(),
        'BevelFilter': dict(),
        'BitmapFilter': dict(),
        'BitmapFilterQuality': dict(),
        'BitmapFilterType': dict(),
        'BlurFilter': dict(),
        'GesturePhase': dict(),
        'ColorMatrixFilter': dict(),
        'HTTPStatusEvent': dict(),
        'ConvolutionFilter': dict(),
        'IEventDispatcher': dict(),
        'DisplacementMapFilter': dict(),
        'IMEEvent': dict(),
        'DisplacementMapFilterMode': dict(),
        'IOErrorEvent': dict(),
        'DropShadowFilter': dict(),
        'KeyboardEvent': dict(),
        'GlowFilter': dict(),
        'MouseEvent': dict(),
        'GradientBevelFilter': dict(),
        'GradientGlowFilter': dict(),
        'ShaderFilter': dict()
    },
    'geom' : {
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
    'globalization' : {
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
    'media' : {
        'AudioDecoder': dict(),
        'Camera': dict(),
        'H264Level': dict(),
        'H264Profile': dict(),
        'H264VideoStreamSettings': dict(),
        'ID3Info': dict(),
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
        'Video': dict(),
        'VideoCodec': dict(),
        'VideoStatus': dict(),
        'VideoStreamSettings': dict()
    },
    'net' : {
        'DynamicPropertyOutput': dict(),
        'FileFilter': dict(),
        'FileReference': dict(),
        'FileReferenceList': dict(),
        'FlashNetScript': dict(),
        'GroupSpecifier': dict(),
        'IDynamicPropertyOutput': dict(),
        'IDynamicPropertyWriter': dict(),
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
        'ObjectEncoding': dict(),
        'Responder': dict(),
        'SecureSocket': dict(),
        'SharedObject': dict(),
        'SharedObjectFlushStatus': dict(),
        'Socket': dict(),
        'URLLoader': dict(),
        'URLLoaderDataFormat': dict(),
        'URLRequest': dict(),
        'URLRequestHeader': dict(),
        'URLRequestMethod': dict(),
        'URLStream': dict(),
        'URLVariables': dict(),
        'XMLSocket': dict()
    },
    'printing' : {
        'PrintJob': dict(),
        'PrintJobOptions': dict(),
        'PrintJobOrientation': dict()
    },
    'profiler' : {
        'Telemetry': dict()
    },
    'sampler' : {
        'ClassFactory': dict(),
        'DeleteObjectSample': dict(),
        'NewObjectSample': dict(),
        'Sample': dict(),
        'StackFrame': dict(),
        'getSize.as': dict()
    },
    'security' : {
        'CertificateStatus': dict(),
        'X500DistinguishedName': dict(),
        'X509Certificate': dict()
    },
    'sensors' : {
        'Accelerometer': dict(),
        'Geolocation': dict(),
    },
    'system' : {
        'ApplicationDomain': dict(),
        'ApplicationInstaller': dict(),
        'AuthorizedFeatures': dict(),
        'AuthorizedFeaturesLoader': dict(),
        'Capabilities': dict(),
        'DomainMemoryWithStage3D': dict(),
        'FSCommand': dict(),
        'IME': dict(),
        'IMEConversionMode': dict(),
        'ImageDecodingPolicy': dict(),
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
        'TouchscreenType': dict()
    },
    'text' : {
        'AntiAliasType': dict(),
        'CSMSettings': dict(),
        'Font': dict(),
        'FontStyle': dict(),
        'FontType': dict(),
        'GridFitType': dict(),
        'StaticText': dict(),
        'StyleSheet': dict(),
        'TextColorType': dict(),
        'TextDisplayMode': dict(),
        'TextExtent': dict(),
        'TextField': dict(),
        'TextFieldAutoSize': dict(),
        'TextFieldType': dict(),
        'TextFormat': dict(),
        'TextFormatAlign': dict(),
        'TextFormatDisplay': dict(),
        'TextInteractionMode': dict(),
        'TextLineMetrics': dict(),
        'TextRenderer': dict(),
        'TextRun': dict(),
        'TextSnapshot': dict()
    },
    'trace' : {
        'Trace': dict()
    },
    'ui' : {
        'ContextMenu': dict(),
        'ContextMenuBuiltInItems': dict(),
        'ContextMenuClipboardItems': dict(),
        'ContextMenuItem': dict(),
        'GameInput': dict(),
        'GameInputControl': dict(),
        'GameInputControlType': dict(),
        'GameInputDevice': dict(),
        'GameInputFinger': dict(),
        'GameInputHand': dict(),
        'KeyLocation': dict(),
        'Keyboard': dict(),
        'KeyboardType': dict(),
        'Mouse': dict(),
        'MouseCursor': dict(),
        'MouseCursorData': dict(),
        'Multitouch': dict(),
        'MultitouchInputMode': dict()
    },
    'utils' : {
        'CompressionAlgorithm': dict(),
        'Endian': dict(),
        'FlashUtilScript': dict(),
        'IDataInput2': dict(),
        'IDataOutput2': dict(),
        'IExternalizable': dict(),
        'SetIntervalTimer': dict(),
        'Timer': dict()
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
                if lines.find('notImplemented(') > 0:
                    featureMatrix[subDirKey][fileKey]['shumway'] = 'Partially' # No
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



# Use registerNativeFunction(' to get a better understanding of what function is
# implemented for each feature (class).


#https://github.com/lightspark/lightspark/blob/318384e22b07375f8432f073bbdb243190b69a88/src/scripting/abc.cpp
#https://github.com/lightspark/lightspark/blob/318384e22b07375f8432f073bbdb243190b69a88/src/allclasses.h
#REGISTER_CLASS_NAME(
#REGISTER_CLASS_NAME2
#All Graphics APIs
#IDrawCommand APIs
#IMEEvent





# Add AwayJS as Flash Player
# https://github.com/awayjs/core/tree/master/lib








#Override features
featureMatrix['display']['Shader']['lightspark'] = 'No'

featureMatrix['display']['Shader']['shumway'] = 'No'
featureMatrix['display']['ShaderInput']['shumway'] = 'No'
featureMatrix['display']['ShaderJob']['shumway'] = 'No'
featureMatrix['display']['ShaderParameter']['shumway'] = 'No'
featureMatrix['display']['ShaderPrecision']['shumway'] = 'No'

  #lightsparkFeatures = []
#dir = './lightspark/src/scripting/flash'
#for subdir, dirs, files in os.walk(dir):
#    for file in files:
#        if file.endswith('.cpp'):
#            fileContent = open(os.path.join(subdir, file), "r")
#            lines = fileContent.read()
#            subDirKey = subdir.replace(dir + '/','')
#            fileKey = file.replace('.cpp', '')
#            if subDirKey in featureMatrix.keys():
#                if lines.find('somewhatImplemented') > 0:
#                    featureMatrix[subDirKey][fileKey]['shumway'] = 'Partially'
#                elif lines.find('notImplemented') > 0:
#                    featureMatrix[subDirKey][fileKey]['shumway'] = 'No'
#                else:
#                    featureMatrix[subDirKey][fileKey]['shumway'] = 'Yes'

#pp = pprint.PrettyPrinter(indent=4,width=280)
#pp.pprint(featureMatrix)

#d_items = featureMatrix.items()
#for key, item in d_items:
#    for key2, item2 in featureMatrix[key].items():
#        print(key2 + '   '
#            '   Flash:    ' + featureMatrix[key][key2]['adobeflash'] +
#            '   Shumway:  ' + featureMatrix[key][key2]['shumway'] +
#            '   LightSpark:   ' + featureMatrix[key][key2]['lightspark'] +
#            '   Gnash:   ' + featureMatrix[key][key2]['gnash']
#        );
#        #print(key2)


with open("flash-matrix.json", "w") as write_file:
    json.dump(featureMatrix, write_file)
