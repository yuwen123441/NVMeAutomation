

from ctypes import Structure, c_uint8, c_uint16, c_uint32, c_uint64, Union


class LBAFormatDataStructure(Union):
    class Bits(Structure):
        _pack_ = 1
        _fields_ = [
            ('metas', c_uint32, 16),    # Metadata Size
            ('lbads', c_uint32, 8),     # LBA Data Size
            ('rp', c_uint32, 2),        # Relative Performance
            ('reserved', c_uint32, 6),
        ]

    _anonymous_ = ('bits', )
    _fields_ = [
        ('dword', c_uint32),
        ('bits', Bits)]

class PowerStateDescriptorDataStructure(Structure):
    _pack_ = 1
    _fields_ = [
        ('mp', c_uint16),           # Active Power Scale
        ('reserved0', c_uint8),
        ('mps', c_uint8, 1),        # Max Power Scale
        ('non_os', c_uint8, 1),     # Non-Operational State
        ('reserved1', c_uint8, 6),
        ('entry_l', c_uint32),      # Entry Latency
        ('exit_l', c_uint32),       # Exit Latency
        ('rrt', c_uint8, 5),        # Relative Read Throughput
        ('reserved2', c_uint8, 3),
        ('rrl', c_uint8, 5),        # Relative Read Latency
        ('reserved3', c_uint8, 3),
        ('rwt', c_uint8, 5),        # Relative Write Throughput
        ('reserved4', c_uint8, 3),
        ('rwl', c_uint8, 5),        # Relative Write Latency
        ('reserved5', c_uint8, 3),
        ('ip', c_uint16),           # Idle Power
        ('reserved6', c_uint8, 6),
        ('ips', c_uint8, 2),        # Idle Power Scale
        ('reserved7', c_uint8),
        ('ap', c_uint16),           # Active Power
        ('apw', c_uint8, 3),        # Active Power Workload
        ('reserved8', c_uint8, 3),
        ('aps', c_uint8, 2),        # Active Power Scale
        ('reserved', (c_uint8 * 9)),
    ]

class NamespaceDataStructure(Structure):
    _pack_ = 1
    _fields_ = [
        ('ns', c_uint64),           # Namespace Size
        ('ncap', c_uint64),         # Namespace Capacity
        ('nuse', c_uint64),         # Namespace Utilization
        ('nsfeat', c_uint8),        # Namespace Features
        ('nlbaf', c_uint8),         # Number of LBA Formats
        ('flbas', c_uint8),         # Formatted LBA Size
        ('mc', c_uint8),            # Metadata Capabilities
        ('dpc', c_uint8),           # End-to-end Data Protection Capabilities
        ('dps', c_uint8),           # End-to-end Data Protection Type Settings
        ('nmic', c_uint8),          # Namespace Multi-path I/O and Namespace Sharing Capabilities
        ('rescap', c_uint8),        # Reservation Capabilities
        ('fpi', c_uint8),           # Format Progress Indicator
        ('dlfeat', c_uint8),
        ('nawun', c_uint16),        # Namespace Atomic Write Unit Normal
        ('nawupf', c_uint16),       # Namespace Atomic Write Unit Power Fail
        ('nacwu', c_uint16),        # Namespace Atomic Compare & Write Unit
        ('nabsn', c_uint16),        # Namespace Atomic Boundary Size Normal
        ('nabo', c_uint16),         # Namespace Atomic Boundary Offset
        ('nabspf', c_uint16),       # Namespace Atomic Boundary Size Power Fail
        ('noiob', (c_uint16)),
        ('nvmcap', (c_uint8 * 16)),                # NVM Capacity:
        ('npwg', (c_uint16)),
        ('npwa', (c_uint16)),
        ('npdg', (c_uint16)),
        ('npda', (c_uint16)),
        ('nows', (c_uint16)),
        ('reserved2', (c_uint8 * 18)),
        ('anagrpid', (c_uint32)),
        ('reserved3', c_uint32, 24),
        ('nsattr', c_uint32, 8),
        ('nvmsetid', c_uint16),
        ('endgid', (c_uint16)),
        ('nguid', (c_uint8 * 16)),                  # Namespace Globally Unique Identifier
        ('eui64', c_uint64),                        # IEEE Extended Unique Identifier
        ('lbaf', LBAFormatDataStructure * 16),      # LBA Format Support
        ('reserved3', (c_uint8 * 192)),
        ('vs', (c_uint8 * 3712)),                   # Vendor Specific
    ]

class ControllerDataStructure(Structure):
    _pack_ = 1
    _fields_ = [
        ('vid', c_uint16),                  # PCI Vendor ID
        ('ssvid', c_uint16),                # PCI Subsystem Vendor ID
        ('serial_num', (c_uint8 * 20)),     # Serial number
        ('model_num', (c_uint8 * 40)),      # Model number for the NVM subsystem
        ('firmware_rev', c_uint64),         # Firmware revision for the NVM subsystem
        ('rab', c_uint8),                   # Recommended Arbitration Burst size
        ('ieee', c_uint32, 24),             # IEEE OUI Identifier
        ('cmic', c_uint32, 8),              # multi-path I/O and namespace sharing capabilities
        ('mdts', c_uint8),                  # maximum data transfer size
        ('cntlid', c_uint16),               # the NVM subsystem unique controller identifier
        ('ver', c_uint32),                  # the value reported in the Version register
        ('rtd3r', c_uint32),                # RTD3 Resume Latency
        ('rtd3e', c_uint32),                # RTD3 Entry Latency
        ('oaes', c_uint32),                 # Optional Asynchronous Events Supported
        ('ctratt', c_uint32),
        ('rrls', c_uint16),
        ('reserved0', (c_uint8 * 9)),
        ('cntrltype', c_uint8),
        ('fguid', (c_uint8 * 16)),
        ('crdt1', (c_uint16)),
        ('crdt2', (c_uint16)),
        ('crdt3', (c_uint16)),
        ('reserved1', (c_uint8 * 106)),
        ('nmis', (c_uint8 * 16)),           # NVMe Management Interface Specification
        ('oacs', c_uint16),                 # Optional Admin Command Support
        ('acl', c_uint8),                   # Abort Command Limit
        ('aerl', c_uint8),                  # Asynchronous Event Request Limit
        ('frmw', c_uint8),             # Firmware Updates
        ('lpa', c_uint8),                   # Log Page Attributes
        ('elpe', c_uint8),                  # Error Log Page Entries
        ('npss', c_uint8),                 # Number of Power States Support
        ('avscc', c_uint8),                 # Admin Vendor Specific Command Configuration
        ('apsta', c_uint8),                 # Autonomous Power State Transition Attributes
        ('wctemp', c_uint16),               # Warning Composite Temperature Threshold
        ('cctemp', c_uint16),               # Critical Composite Temperature Threshold
        ('mtfa', c_uint16),                 # Maximum Time for Firmware Activation
        ('hmpre', c_uint32),                # Host Memory Buffer Preferred Size
        ('hmmin', c_uint32),                # Host Memory Buffer Minimum Size
        ('tnvmcap', (c_uint8 * 16)),        # Total NVM Capacity
        ('unvmcap', (c_uint8 * 16)),        # Unallocated NVM Capacity
        ('rpmbs', c_uint32),                # Replay Protected Memory Block Support
        ('edstt', (c_uint16)),
        ('dsto', (c_uint8)),
        ('fwug', (c_uint8)),
        ('kas', (c_uint16)),
        ('hctma', (c_uint16)),
        ('mntmt', (c_uint16)),
        ('mxtmt', (c_uint16)),
        ('sanicap', (c_uint32)),
        ('hmminds', (c_uint32)),
        ('hmmaxd', (c_uint16)),
        ('nsetidmax', (c_uint16)),
        ('endgidmax', (c_uint16)),
        ('anatt', (c_uint8)),
        ('anacap', (c_uint8)),
        ('anagrpmax', (c_uint32)),
        ('nanagrpid', (c_uint32)),
        ('pels', (c_uint32)),
        ('reserved2', (c_uint8 * 156)),
        ('sqes', c_uint8),                  # Submission Queue Entry Size
        ('cqes', c_uint8),                  # Completion Queue Entry Size
        ('maxcmd', (c_uint16)),
        ('nn', (c_uint32)),                # Number of Namespaces
        ('oncs', (c_uint16)),              # Optional NVM Command Support
        ('fuses', (c_uint16)),             # Fused Operation Support
        ('fna', (c_uint8)),               # Format NVM Attributes
        ('vwc', (c_uint8)),               # Volatile Write Cache
        ('awun', c_uint16),                 # Atomic Write Unit Normal
        ('awupf', c_uint16),                # Atomic Write Unit Power Fail
        ('nvscc', c_uint8),               # NVM Vendor Specific Command Configuration
        ('nwpc', (c_uint8)),
        ('acwu', c_uint16),                 # Atomic Compare & Write Unit
        ('reserved3', (c_uint16)),
        ('sgls', c_uint32),                 # SGL Support
        ('mnan', (c_uint32)),
        ('reserved4', (c_uint8 * 224)),
        ('subnqn', (c_uint8 * 256)),
        ('reserved5', (c_uint8 * 768)),
        ('nvmeof', (c_uint8 * 256)),
        ('psd', PowerStateDescriptorDataStructure * 32),    # Power State Descriptor
        ('vs', (c_uint8 * 1024)),                           # Vendor Specific
    ]

class NVMSetAttributesEntry(Structure):
    """Identify - Power State Descriptor Data Structure"""
    _pack_ = 1
    _fields_ = [
        ('nvmsetid', c_uint16),           # Active Power Scale
        ('egid', c_uint16),
        ('reserved', c_uint32),        # Max Power Scale
        ('4krrt', c_uint32),     # Non-Operational State
        ('ows', c_uint32),
        ('tnvmsetcap', (c_uint8 * 16)),      # Entry Latency
        ('unvmsetcap', (c_uint8 * 16)),       # Exit Latency
        ('reserved', (c_uint8*80)),        # Relative Read Throughput
    ]

class NVMSetList(Structure):
    """Identify - Power State Descriptor Data Structure"""
    _pack_ = 1
    _fields_ = [
        ('ni', c_uint8),           # Number of Identifiers
        ('reserved0', c_uint8*127),
        ('entry', NVMSetAttributesEntry*31),        # NVM Set Attributes Entry
    ]


class PrimaryControllerCap(Structure):
    """Identify - Power State Descriptor Data Structure"""
    _pack_ = 1
    _fields_ = [
        ('cntlid', c_uint16),           # Number of Identifiers
        ('portid', c_uint16),
        ('crt', c_uint8),
        ('reserved0', c_uint8*27),
        ('vqfrt', c_uint32),
        ('vqrfa', c_uint32),
        ('vqrfap', c_uint16),
        ('vqprt', c_uint16),
        ('vqfrsm', c_uint16),
        ('vqgran', c_uint16),
        ('reserved1', c_uint8*16),
        ('vifrt', c_uint32),
        ('virfa', c_uint32),
        ('virfap', c_uint16),
        ('viprt', c_uint16),
        ('vifrsm', c_uint16),
        ('vigran', c_uint16),
        ('reserved2', c_uint8*4016),        # NVM Set Attributes Entry
    ]


class SecondaryControllerListEntry(Structure):
    """Identify - Power State Descriptor Data Structure"""
    _pack_ = 1
    _fields_ = [
        ('scid', c_uint16),           # Number of Identifiers
        ('pcid', c_uint16),
        ('scs', c_uint8),
        ('reserved0', c_uint8*3),
        ('vfn', c_uint16),
        ('nvq', c_uint16),
        ('nvi', c_uint16),
        ('reserved1', c_uint8*18),
    ]

class SecondaryControllerList(Structure):
    """Identify - Power State Descriptor Data Structure"""
    _pack_ = 1
    _fields_ = [
        ('ni', c_uint8),           # Number of Identifiers
        ('reserved0', c_uint8*31),
        ('entry', SecondaryControllerListEntry*127),
    ]
