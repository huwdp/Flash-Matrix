#!/usr/bin/env python
import os
import pprint
import json
import re
import datetime
import re


fileName = 'flash-matrix.json'
dt_date = datetime.datetime.now()

#ArgumentError
#Array
#Boolean
#Class
#Date
#DefinitionError
#Error
#EvalError
#Function
#int
#JSON
#Math
#Namespace
#Number
#Object
#QName
#RangeError
#ReferenceError
#RegExp
#SecurityError
#String
#SyntaxError
#TypeError
#uint
#UninitializedError
#URIError
#VerifyError
#XML
#XMLList

featureMatrix = {
    'modifiedOn': dt_date.strftime("%A, %d %b %Y"),
    'matrix':
    {
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
        'concurrent': {
            'Condition': dict(),
            'Mutex': dict()
        },
        'crypto': {
            'crypto': dict()
        },
        'desktop' : { # Checked
            'Clipboard':dict(),
            'ClipboardFormats':dict(),
            'ClipboardTransferMode':dict(),
            #'IFilePromise':dict()  AIR
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
            'AVLoader': dict(),
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
        'display3D.textures': {
            'CubeTexture': dict(),
            'RectangleTexture': dict(),
            'Texture': dict(),
            'TextureBase': dict(),
            'VideoTexture': dict()
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
            'AudioOutputChangeEvent': dict(),
            'AVDictionaryDataEvent': dict(),
            'AVHTTPStatusEvent': dict(),
            'AVPauseAtPeriodEndEvent': dict(),
            # BrowserInvokeEvent AIR
            'ContextMenuEvent': dict(),
            'DataEvent': dict(),
            'DRMAuthenticationCompleteEvent': dict(),
            'DRMAuthenticationErrorEvent': dict(),
            #'DRMAuthenticateEvent': dict(), AIR
            'DRMDeviceGroupErrorEvent': dict(),
            'DRMDeviceGroupEvent': dict(),
            'DRMErrorEvent': dict(),
            'DRMLicenseRequestEvent': dict(),
            'DRMMetadataEvent': dict(),
            'DRMReturnVoucherCompleteEvent': dict(),
            'DRMReturnVoucherErrorEvent': dict(),
            'DRMStatusEvent': dict(),
            'ErrorEvent': dict(),
            'Event': dict(),
            'EventDispatcher': dict(),
            'EventPhase': dict(),
            'FocusEvent': dict(),
            'FullScreenEvent': dict(),
            #'GameInputEvent': dict(), AIR
            #'GeolocationEvent': dict(), AIR/FlashLite
            'GestureEvent': dict(),
            'GesturePhase': dict(),
            'Geolocation': dict(),
            'HTTPStatusEvent': dict(),
            'IEventDispatcher': dict(),
            'IMEEvent': dict(),
            'IOErrorEvent': dict(),
            'KeyboardEvent': dict(),
            'MouseEvent': dict(),
            'NetDataEvent': dict(),
            'NetMonitorEvent': dict(),
            'NetStatusEvent': dict(),
            #'OutputProgressEvent': dict(), AIR
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
            #'DatagramSocket': dict(), AIR
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
            #'URLRequestDefaults': dict(), AIR
            'URLRequestHeader': dict(),
            'URLRequestMethod': dict(),
            'URLStream': dict(),
            'URLVariables': dict(),
            'XMLSocket': dict()
        },
        'net.drm': {
            'AuthenticationMethod': dict(),
            'DRMContentData': dict(),
            'DRMDeviceGroup': dict(),
            'DRMManager': dict(),
            'DRMPlaybackTimeWindow': dict(),
            'DRMVoucher': dict(),
            'LoadVoucherSetting': dict(),
            'VoucherAccessInfo': dict()
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
            #'ReferencesValidationSetting': dict(), AIR
            #'RevocationCheckSettings': dict(), AIR
            #'SignatureStatus': dict(), AIR
            #'SignerTrustSettings': dict(), AIR
            'X500DistinguishedName': dict(),
            'X509Certificate': dict(),
            #'XMLSignatureValidator': dict(), AIR
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
        'text.engine': {
            'BreakOpportunity': dict(),
            'CFFHinting': dict(),
            'ContentElement': dict(),
            'DigitCase': dict(),
            'DigitWidth': dict(),
            'EastAsianJustifier': dict(),
            'ElementFormat': dict(),
            'FontDescription': dict(),
            'FontLookup': dict(),
            'FontMetrics': dict(),
            'FontPosture': dict(),
            'FontWeight': dict(),
            'GraphicElement': dict(),
            'GroupElement': dict(),
            'JustificationStyle': dict(),
            'Kerning': dict(),
            'LigatureLevel': dict(),
            'LineJustification': dict(),
            'RenderingMode': dict(),
            'SpaceJustifier': dict(),
            'TabAlignment': dict(),
            'TabStop': dict(),
            'TextBaseline': dict(),
            'TextBlock': dict(),
            'TextElement': dict(),
            'TextJustifier': dict(),
            'TextLine': dict(),
            'TextLineCreationResult': dict(),
            'TextLineMirrorRegion': dict(),
            'TextLineValidity': dict(),
            'TextRotation': dict(),
            'TypographicCase': dict()
        },
        'text.ime': {
            'CompositionAttributeRange': dict(),
            'IIMEClient': dict()
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
            'IExternalizable': dict(),
            'Timer': dict(),
            'ByteArray': dict(),
            'Dictionary': dict(),
            'Proxy': dict()
        },
        'xml': {
            'XMLDocument': dict(),
            'XMLNode': dict(),
            'XMLNodeType': dict()
        }
    }
}

matrix = featureMatrix['matrix']

# Add Flash Players to matrix
for category in matrix:
    for feature in matrix[category]:
        matrix[category][feature] = {'adobeflash' : 'Yes', 'shumway' : 'No', 'lightspark': 'No', 'gnash': 'No', 'ruffle': 'No', 'awayfl': 'No'}

#==================Parse Flash Players for stats==================

# Parse AwayFL Files
dir = './playerglobal/lib'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.ts'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            subDirKey = subdir.replace(dir + '/','').replace('/', '.')
            fileKey = file.replace('.ts', '')
            if subDirKey in matrix.keys():
                if fileKey in matrix[subDirKey].keys():
                    #if  lines.find('// @todo"'):
                    #    matrix[subDirKey][fileKey]['awayfl'] = 'Partially'
                    if lines.find('not implemented') > 0:
                        matrix[subDirKey][fileKey]['awayfl'] = 'Partially' # No
                    else:
                        matrix[subDirKey][fileKey]['awayfl'] = 'Yes'

#  Parse Shumway files
dir = './shumway/src/flash'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.ts'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            subDirKey = subdir.replace(dir + '/','').replace('/', '.')
            fileKey = file.replace('.ts', '')
            if subDirKey in matrix.keys():
                if fileKey in matrix[subDirKey].keys():
                    if lines.find('somewhatImplemented(') > 0:
                        matrix[subDirKey][fileKey]['shumway'] = 'Partially'
                    elif lines.find('notImplemented(') > 0:
                        matrix[subDirKey][fileKey]['shumway'] = 'Partially' # No
                    else:
                        matrix[subDirKey][fileKey]['shumway'] = 'Yes'

# Use https://github.com/mozilla/shumway/blob/16451d8836fa85f4b16eeda8b4bda2fa9e2b22b0/utils/playerglobal-builder/manifest.json
# for better understanding of what is supported.

# Parse Gnash files

dir = './gnash/libcore/'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.cpp'):
            fileKey = file.replace('.cpp', '')
            for item in matrix:
                if fileKey in matrix[item].keys():
                    matrix[item][fileKey]['gnash'] = 'Partially'
        if file.endswith('_as.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            subDirKey = subdir.replace(dir + '/','')
            fileKey = file.replace('_as.cpp', '')
            for item in matrix:
                if fileKey in matrix[item].keys():
                    matrix[item][fileKey]['gnash'] = 'Yes'

# Parse Lightspark files
# Find Lightspark features
lightsparkRegisters = [
"./lightspark/src/scripting/abc_avm1.cpp",
"./lightspark/src/scripting/abc_flashaccessibility.cpp",
"./lightspark/src/scripting/abc_flashdesktop.cpp",
"./lightspark/src/scripting/abc_flashconcurrent.cpp",
"./lightspark/src/scripting/abc_flashcrypto.cpp",
"./lightspark/src/scripting/abc_flashdisplay.cpp",
"./lightspark/src/scripting/abc_flashdisplay3d.cpp",
"./lightspark/src/scripting/abc_flashevents.cpp",
"./lightspark/src/scripting/abc_flasherrors.cpp",
"./lightspark/src/scripting/abc_flashexternal.cpp",
"./lightspark/src/scripting/abc_flashfilesystem.cpp",
"./lightspark/src/scripting/abc_flashfilters.cpp",
"./lightspark/src/scripting/abc_flashgeom.cpp",
"./lightspark/src/scripting/abc_flashglobalization.cpp",
"./lightspark/src/scripting/abc_flashmedia.cpp",
"./lightspark/src/scripting/abc_flashnet.cpp",
"./lightspark/src/scripting/abc_flashprinting.cpp",
"./lightspark/src/scripting/abc_flashsampler.cpp",
"./lightspark/src/scripting/abc_flashsecurity.cpp",
"./lightspark/src/scripting/abc_flashsensors.cpp",
"./lightspark/src/scripting/abc_flashsystem.cpp",
"./lightspark/src/scripting/abc_flashtext.cpp",
"./lightspark/src/scripting/abc_flashui.cpp",
"./lightspark/src/scripting/abc_flashutils.cpp",
"./lightspark/src/scripting/abc_flashxml.cpp",
"./lightspark/src/scripting/abc_avmplus.cpp",
"./lightspark/src/scripting/abc_toplevel.cpp",
]

for file in lightsparkRegisters:
    fileContent = open(file, "r")
    lines = fileContent.read()
    matches = re.findall('builtin\-\>registerBuiltin\("(\w+)",', lines)
    for item in matrix:
        for match in matches:
            if match in matrix[item].keys():
                matrix[item][match]['lightspark'] = 'Yes'

# Find "Not implemented in all features to set as partially complete"
dir = './lightspark/src/scripting/'
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.cpp'):
            fileContent = open(os.path.join(subdir, file), "r")
            lines = fileContent.read()
            matches = re.findall('LOG\(LOG_NOT_IMPLEMENTED,\"(\w+) is not implemented', lines)
            for item in matrix:
                for match in matches:
                    if match in matrix[item].keys():
                        matrix[item][match]['lightspark'] = 'Partially' # No
            matches = re.findall('LOG\(LOG_NOT_IMPLEMENTED,\"(\w+)\.', lines)
            for item in matrix:
                for match in matches:
                    if match in matrix[item].keys():
                        matrix[item][match]['lightspark'] = 'Partially'
            matches = re.findall('ASFUNCTIONBODY_GETTER_NOT_IMPLEMENTED\((\w+)\,', lines)
            for item in matrix:
                for match in matches:
                    if match in matrix[item].keys():
                        matrix[item][match]['lightspark'] = 'Partially'

matrix['crypto']['crypto']['lightspark'] = 'Yes'

# Parse Ruffle files

dir = './ruffle/core/src/avm2/globals/flash/'

def ruffleFileKey(fileName):
    fileKey = fileName.replace('.rs', '')
    fileKey = fileKey.replace('.as', '')
    fileKey = fileKey.lower()
    fileKey = re.sub(r'[^a-zA-Z0-9]', '', fileKey)
    return fileKey

# We assume here that if the file exists then it is implemented 100%
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.rs') or file.endswith('.as'):
            fileKey = ruffleFileKey(file)
            for item in matrix:
                for key, value in matrix[item].items():
                    if fileKey.lower() == key.lower():
                        matrix[item][key]['ruffle'] = 'Yes'

# Find "Not implemented in all features to set as partially complete"
for subdir, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.rs') or file.endswith('.as'):
            fileReader = open(os.path.join(subdir, file), "r")
            content = fileReader.read()
            lines = content.split(";")
            for line in lines:
                matches = re.findall('stub_.*?\(.*?\"(?:[^.]*\.)*(.*?)\"', line)
                for item in matrix:
                    for match in matches:
                        if match in matrix[item].keys():
                            matrix[item][match]['ruffle'] = 'Partially'

# Override some features
matrix['trace']['Trace']['lightspark'] = 'Yes'
matrix['display']['Shader']['lightspark'] = 'No'
matrix['display']['Shader']['shumway'] = 'No'
matrix['display']['ShaderInput']['shumway'] = 'No'
matrix['display']['ShaderJob']['shumway'] = 'No'
matrix['display']['ShaderParameter']['shumway'] = 'No'
matrix['display']['ShaderPrecision']['shumway'] = 'No'
matrix['trace']['Trace']['ruffle'] = 'Yes'

with open(fileName, "r") as read_file:
    existingFeatureMatrix = json.load(read_file)

if (sorted(existingFeatureMatrix['matrix'].items()) != sorted(featureMatrix['matrix'].items())):
    print("File is differnet.")

with open(fileName, "w") as write_file:
    json.dump(featureMatrix, write_file ,indent = 2)
