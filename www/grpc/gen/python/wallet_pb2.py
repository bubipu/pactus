# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cwallet.proto\x12\x06pactus\"O\n\x17GenerateMnemonicRequest\x12\x18\n\x07\x65ntropy\x18\x01 \x01(\x05R\x07\x65ntropy\x12\x1a\n\x08language\x18\x02 \x01(\tR\x08language\"6\n\x18GenerateMnemonicResponse\x12\x1a\n\x08mnemonic\x18\x01 \x01(\tR\x08mnemonic\"}\n\x13\x43reateWalletRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08mnemonic\x18\x02 \x01(\tR\x08mnemonic\x12\x1a\n\x08language\x18\x03 \x01(\tR\x08language\x12\x1a\n\x08password\x18\x04 \x01(\tR\x08password\"\x16\n\x14\x43reateWalletResponse2\xaa\x01\n\x06Wallet\x12U\n\x10GenerateMnemonic\x12\x1f.pactus.GenerateMnemonicRequest\x1a .pactus.GenerateMnemonicResponse\x12I\n\x0c\x43reateWallet\x12\x1b.pactus.CreateWalletRequest\x1a\x1c.pactus.CreateWalletResponseBA\n\rpactus.walletZ0github.com/pactus-project/pactus/www/grpc/pactusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wallet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rpactus.walletZ0github.com/pactus-project/pactus/www/grpc/pactus'
  _GENERATEMNEMONICREQUEST._serialized_start=24
  _GENERATEMNEMONICREQUEST._serialized_end=103
  _GENERATEMNEMONICRESPONSE._serialized_start=105
  _GENERATEMNEMONICRESPONSE._serialized_end=159
  _CREATEWALLETREQUEST._serialized_start=161
  _CREATEWALLETREQUEST._serialized_end=286
  _CREATEWALLETRESPONSE._serialized_start=288
  _CREATEWALLETRESPONSE._serialized_end=310
  _WALLET._serialized_start=313
  _WALLET._serialized_end=483
# @@protoc_insertion_point(module_scope)