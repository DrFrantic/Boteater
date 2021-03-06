#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def getProductV2(self, request):
        """
        Parameters:
         - request

        """
        pass

    def getProduct(self, shopId, productId, locale):
        """
        Parameters:
         - shopId
         - productId
         - locale

        """
        pass

    def getShowcaseV3(self, showcaseRequest):
        """
        Parameters:
         - showcaseRequest

        """
        pass

    def placePurchaseOrderForFreeProduct(self, purchaseOrder):
        """
        Parameters:
         - purchaseOrder

        """
        pass

    def placePurchaseOrderWithLineCoin(self, purchaseOrder):
        """
        Parameters:
         - purchaseOrder

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getProductV2(self, request):
        """
        Parameters:
         - request

        """
        self.send_getProductV2(request)
        return self.recv_getProductV2()

    def send_getProductV2(self, request):
        self._oprot.writeMessageBegin('getProductV2', TMessageType.CALL, self._seqid)
        args = getProductV2_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProductV2(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProductV2_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProductV2 failed: unknown result")

    def getProduct(self, shopId, productId, locale):
        """
        Parameters:
         - shopId
         - productId
         - locale

        """
        self.send_getProduct(shopId, productId, locale)
        return self.recv_getProduct()

    def send_getProduct(self, shopId, productId, locale):
        self._oprot.writeMessageBegin('getProduct', TMessageType.CALL, self._seqid)
        args = getProduct_args()
        args.shopId = shopId
        args.productId = productId
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProduct failed: unknown result")

    def getShowcaseV3(self, showcaseRequest):
        """
        Parameters:
         - showcaseRequest

        """
        self.send_getShowcaseV3(showcaseRequest)
        return self.recv_getShowcaseV3()

    def send_getShowcaseV3(self, showcaseRequest):
        self._oprot.writeMessageBegin('getShowcaseV3', TMessageType.CALL, self._seqid)
        args = getShowcaseV3_args()
        args.showcaseRequest = showcaseRequest
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getShowcaseV3(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getShowcaseV3_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getShowcaseV3 failed: unknown result")

    def placePurchaseOrderForFreeProduct(self, purchaseOrder):
        """
        Parameters:
         - purchaseOrder

        """
        self.send_placePurchaseOrderForFreeProduct(purchaseOrder)
        return self.recv_placePurchaseOrderForFreeProduct()

    def send_placePurchaseOrderForFreeProduct(self, purchaseOrder):
        self._oprot.writeMessageBegin('placePurchaseOrderForFreeProduct', TMessageType.CALL, self._seqid)
        args = placePurchaseOrderForFreeProduct_args()
        args.purchaseOrder = purchaseOrder
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_placePurchaseOrderForFreeProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = placePurchaseOrderForFreeProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "placePurchaseOrderForFreeProduct failed: unknown result")

    def placePurchaseOrderWithLineCoin(self, purchaseOrder):
        """
        Parameters:
         - purchaseOrder

        """
        self.send_placePurchaseOrderWithLineCoin(purchaseOrder)
        return self.recv_placePurchaseOrderWithLineCoin()

    def send_placePurchaseOrderWithLineCoin(self, purchaseOrder):
        self._oprot.writeMessageBegin('placePurchaseOrderWithLineCoin', TMessageType.CALL, self._seqid)
        args = placePurchaseOrderWithLineCoin_args()
        args.purchaseOrder = purchaseOrder
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_placePurchaseOrderWithLineCoin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = placePurchaseOrderWithLineCoin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "placePurchaseOrderWithLineCoin failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getProductV2"] = Processor.process_getProductV2
        self._processMap["getProduct"] = Processor.process_getProduct
        self._processMap["getShowcaseV3"] = Processor.process_getShowcaseV3
        self._processMap["placePurchaseOrderForFreeProduct"] = Processor.process_placePurchaseOrderForFreeProduct
        self._processMap["placePurchaseOrderWithLineCoin"] = Processor.process_placePurchaseOrderWithLineCoin
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_getProductV2(self, seqid, iprot, oprot):
        args = getProductV2_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProductV2_result()
        try:
            result.success = self._handler.getProductV2(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ShopExecption as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getProductV2", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProduct(self, seqid, iprot, oprot):
        args = getProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProduct_result()
        try:
            result.success = self._handler.getProduct(args.shopId, args.productId, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ShopExecption as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getShowcaseV3(self, seqid, iprot, oprot):
        args = getShowcaseV3_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getShowcaseV3_result()
        try:
            result.success = self._handler.getShowcaseV3(args.showcaseRequest)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ShopExecption as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getShowcaseV3", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_placePurchaseOrderForFreeProduct(self, seqid, iprot, oprot):
        args = placePurchaseOrderForFreeProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = placePurchaseOrderForFreeProduct_result()
        try:
            result.success = self._handler.placePurchaseOrderForFreeProduct(args.purchaseOrder)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ShopExecption as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("placePurchaseOrderForFreeProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_placePurchaseOrderWithLineCoin(self, seqid, iprot, oprot):
        args = placePurchaseOrderWithLineCoin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = placePurchaseOrderWithLineCoin_result()
        try:
            result.success = self._handler.placePurchaseOrderWithLineCoin(args.purchaseOrder)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ShopExecption as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("placePurchaseOrderWithLineCoin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getProductV2_args(object):
    """
    Attributes:
     - request

    """


    def __init__(self, request=None,):
        self.request = request

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.request = GetProductRequest()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProductV2_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProductV2_args)
getProductV2_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [GetProductRequest, None], None, ),  # 2
)


class getProductV2_result(object):
    """
    Attributes:
     - success
     - e

    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = GetProductV2Response()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ShopExecption()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProductV2_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProductV2_result)
getProductV2_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GetProductV2Response, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ShopExecption, None], None, ),  # 1
)


class getProduct_args(object):
    """
    Attributes:
     - shopId
     - productId
     - locale

    """


    def __init__(self, shopId=None, productId=None, locale=None,):
        self.shopId = shopId
        self.productId = productId
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.shopId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.locale = Locale()
                    self.locale.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProduct_args')
        if self.shopId is not None:
            oprot.writeFieldBegin('shopId', TType.STRING, 2)
            oprot.writeString(self.shopId.encode('utf-8') if sys.version_info[0] == 2 else self.shopId)
            oprot.writeFieldEnd()
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 3)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRUCT, 4)
            self.locale.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProduct_args)
getProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'shopId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'productId', 'UTF8', None, ),  # 3
    (4, TType.STRUCT, 'locale', [Locale, None], None, ),  # 4
)


class getProduct_result(object):
    """
    Attributes:
     - success
     - e

    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Product()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ShopExecption()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProduct_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProduct_result)
getProduct_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Product, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ShopExecption, None], None, ),  # 1
)


class getShowcaseV3_args(object):
    """
    Attributes:
     - showcaseRequest

    """


    def __init__(self, showcaseRequest=None,):
        self.showcaseRequest = showcaseRequest

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.showcaseRequest = ShowcaseRequest()
                    self.showcaseRequest.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getShowcaseV3_args')
        if self.showcaseRequest is not None:
            oprot.writeFieldBegin('showcaseRequest', TType.STRUCT, 1)
            self.showcaseRequest.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getShowcaseV3_args)
getShowcaseV3_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'showcaseRequest', [ShowcaseRequest, None], None, ),  # 1
)


class getShowcaseV3_result(object):
    """
    Attributes:
     - success
     - e

    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ShowcaseV3Response()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ShopExecption()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getShowcaseV3_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getShowcaseV3_result)
getShowcaseV3_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ShowcaseV3Response, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ShopExecption, None], None, ),  # 1
)


class placePurchaseOrderForFreeProduct_args(object):
    """
    Attributes:
     - purchaseOrder

    """


    def __init__(self, purchaseOrder=None,):
        self.purchaseOrder = purchaseOrder

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.purchaseOrder = PurchaseOrder()
                    self.purchaseOrder.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('placePurchaseOrderForFreeProduct_args')
        if self.purchaseOrder is not None:
            oprot.writeFieldBegin('purchaseOrder', TType.STRUCT, 2)
            self.purchaseOrder.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(placePurchaseOrderForFreeProduct_args)
placePurchaseOrderForFreeProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'purchaseOrder', [PurchaseOrder, None], None, ),  # 2
)


class placePurchaseOrderForFreeProduct_result(object):
    """
    Attributes:
     - success
     - e

    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PurchaseOrderResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ShopExecption()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('placePurchaseOrderForFreeProduct_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(placePurchaseOrderForFreeProduct_result)
placePurchaseOrderForFreeProduct_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PurchaseOrderResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ShopExecption, None], None, ),  # 1
)


class placePurchaseOrderWithLineCoin_args(object):
    """
    Attributes:
     - purchaseOrder

    """


    def __init__(self, purchaseOrder=None,):
        self.purchaseOrder = purchaseOrder

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.purchaseOrder = PurchaseOrder()
                    self.purchaseOrder.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('placePurchaseOrderWithLineCoin_args')
        if self.purchaseOrder is not None:
            oprot.writeFieldBegin('purchaseOrder', TType.STRUCT, 2)
            self.purchaseOrder.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(placePurchaseOrderWithLineCoin_args)
placePurchaseOrderWithLineCoin_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'purchaseOrder', [PurchaseOrder, None], None, ),  # 2
)


class placePurchaseOrderWithLineCoin_result(object):
    """
    Attributes:
     - success
     - e

    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PurchaseOrderResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ShopExecption()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('placePurchaseOrderWithLineCoin_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(placePurchaseOrderWithLineCoin_result)
placePurchaseOrderWithLineCoin_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PurchaseOrderResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ShopExecption, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

