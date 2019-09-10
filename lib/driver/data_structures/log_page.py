from ctypes import Structure, c_uint8, c_uint16, c_uint32, c_uint64, Union


class ErrorInformation(Structure):
    """Get Log Page - Error Information (Log Identifier 01h)"""
    _pack_ = 1
    _fields_ = [
        ('ec', c_uint64),           # Error Count
        ('sqid', c_uint16),         # Submission Queue ID
        ('cmdid', c_uint16),        # Command ID
        ('sf', c_uint16),           # Status Field
        ('pel', c_uint16),          # Parameter Error Location
        ('lba', c_uint64),          # LBA
        ('ns', c_uint32),           # Namespace
        ('vsia', c_uint32, 8),      # Vendor Specific Information Available
        ('rsv0', c_uint32, 24),     # Reserve Field 0
        ('cmdsi', c_uint64),        # Command Specific Information
        ('rsv1', c_uint8 * 24),     # Reserve Field 1
    ]

class SmartHealth(Structure):
    """Get Log Page - SMART/Health Information (Log Identifier 02h)"""
    _pack_ = 1
    _fields_ = [
        ('cw', c_uint8),            # Critical Warning
        ('ct', c_uint16),           # Composite Temperature
        ('aspare', c_uint8),        # Available Spare
        ('asparet', c_uint8),       # Available Spare Threshold
        ('prctu', c_uint8),         # Percentage Used
        ('egcws', c_uint8),         # Endurance Group Critical Warning Summary
        ('rsv0', c_uint8 * 25),     # Reserve field 0
        ('dur', c_uint64 * 2),      # Data Units Read
        ('duw', c_uint64 * 2),      # Data Units Write
        ('hrc', c_uint64 * 2),      # Host Read Commands
        ('hwc', c_uint64 * 2),      # Host Write Commands
        ('cbt', c_uint64 * 2),      # Controller Busy Time
        ('pc', c_uint64 * 2),       # Power Cycles
        ('ponh', c_uint64 * 2),     # Power On Hours
        ('ussd', c_uint64 * 2),     # Unsafe Shutdowns
        ('mdie', c_uint64 * 2),     # Number of Error Information Log Entries
        ('neile', c_uint64 * 2),    # Media and Data Integrity Errors
        ('wctt', c_uint32),         # Warning Composite Temperature Time
        ('cctt', c_uint32),         # Critical Composite Temperature Time
        ('ts1', c_uint16),          # Temperature Sensor 1
        ('ts2', c_uint16),          # Temperature Sensor 2
        ('ts3', c_uint16),          # Temperature Sensor 3
        ('ts4', c_uint16),          # Temperature Sensor 4
        ('ts5', c_uint16),          # Temperature Sensor 5
        ('ts6', c_uint16),          # Temperature Sensor 6
        ('ts7', c_uint16),          # Temperature Sensor 7
        ('ts8', c_uint16),          # Temperature Sensor 8
        ('rsv1', c_uint8 * 296),    # Reserve field 1
    ]


class FirmwareSlotInformationLog(Structure):
    """Get Log Page - Firmware Slot Information Log (Log Identifier 03h)"""
    _pack_ = 1
    _fields_ = [
        ('afi', c_uint8),           # Active Firmware Info
        ('rsv0', c_uint8 * 7),      # Reserve field 0
        ('fwrev1', c_uint8 * 8),    # Firmware Revision for Slot 1
        ('fwrev2', c_uint8 * 8),    # Firmware Revision for Slot 2
        ('fwrev3', c_uint8 * 8),    # Firmware Revision for Slot 3
        ('fwrev4', c_uint8 * 8),    # Firmware Revision for Slot 4
        ('fwrev5', c_uint8 * 8),    # Firmware Revision for Slot 5
        ('fwrev6', c_uint8 * 8),    # Firmware Revision for Slot 6
        ('fwrev7', c_uint8 * 8),    # Firmware Revision for Slot 7
        ('rsv1', c_uint8 * 448),    # Reserve field 1
    ]


class ChangedNamespaceList(Structure):
    """Get Log Page - Changed Namespace List (Log Identifier 04h)"""
    _pack_ = 1
    _fields_ = [
        ('entry', c_uint32 * 1024),
    ]


class CommandEffectDataStructure(Structure):
    """Get Log Page - Command Effect Data Structure (Log Identifier 05h)"""
    _pack_ = 1
    _fields_ = [
        ('csupp', c_uint32, 1),
        ('lbcc', c_uint32, 1),
        ('ncc', c_uint32, 1),
        ('nic', c_uint32, 1),
        ('ccc', c_uint32, 1),
        ('rsv0', c_uint32, 11),
        ('cse', c_uint32, 3),
        ('rsv1', c_uint32, 13),
    ]


class CommandEffectLog(Structure):
    """Get Log Page - Command Effect Log (Log Identifier 05h)"""
    _pack_ = 1
    _fields_ = [
        ('acs', CommandEffectDataStructure * 256),
        ('iocs', CommandEffectDataStructure * 256),
        ('rsv', c_uint8 * 2048),
    ]


class SelfTestResultDataStructure(Structure):
    """Get Log Page - Reservation Notification (Log Identifier 80h)"""
    _pack_ = 1
    _fields_ = [
        ('dsts', c_uint8),
        ('sn', c_uint8),
        ('vdi', c_uint8),
        ('rsv0', c_uint8),
        ('poh', c_uint64),
        ('nsid', c_uint32),
        ('flba', c_uint64),
        ('sct', c_uint8),
        ('sc', c_uint8),
        ('vs', c_uint16)
    ]

class SelfTestLog(Structure):
    """Get Log Page - Reservation Notification (Log Identifier 80h)"""
    _pack_ = 1
    _fields_ = [
        ('cdsto', c_uint8),
        ('cdstc', c_uint8),
        ('rsv0', c_uint16),
        ('entry', SelfTestResultDataStructure*20),
    ]

class TelemetryHostInitiatedLog(Structure):
    """Get Log Page - Reservation Notification (Log Identifier 80h)"""
    _pack_ = 1
    _fields_ = [
        ('lid', c_uint8),
        ('rsv0', c_uint8*3),
        ('rsv1', c_uint32, 8),
        ('ieee', c_uint32, 24),
        ('hida1', c_uint16),
        ('hida2', c_uint16),
        ('hida3', c_uint16),
        ('rsv2', c_uint8*368),
        ('cida', c_uint8),
        ('cidgn', c_uint8),
        ('ri', c_uint8*128),
        ('hidb1', c_uint8*512),
        ('hidb2', c_uint8*512),
    ]

class TelemetryControllerInitiatedLog(Structure):
    """Get Log Page - Reservation Notification (Log Identifier 80h)"""
    _pack_ = 1
    _fields_ = [
        ('lid', c_uint8),
        ('rsv0', c_uint8*3),
        ('rsv1', c_uint32, 8),
        ('ieee', c_uint32, 24),
        ('cida1', c_uint16),
        ('cida2', c_uint16),
        ('cida3', c_uint16),
        ('rsv2', c_uint8*368),
        ('cida', c_uint8),
        ('cidgn', c_uint8),
        ('ri', c_uint8*128),
        ('cidb1', c_uint8*512),
        ('cidb2', c_uint8*512),
    ]


class SanitizeStatusLog(Structure):
    """Get Log Page - Reservation Notification (Log Identifier 80h)"""
    _pack_ = 1
    _fields_ = [
        ('sprog', c_uint16),
        ('sstat', c_uint16),
        ('scdw10', c_uint32),
        ('etfo', c_uint32),
        ('etfbe', c_uint32),
        ('etfce', c_uint32),
        ('etfownd', c_uint32),
        ('etfbewnd', c_uint32),
        ('etfcewnd', c_uint32),
        ('rsv0', c_uint8*480),
    ]
