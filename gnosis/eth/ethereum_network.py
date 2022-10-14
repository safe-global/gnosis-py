from enum import Enum, unique


class EthereumNetworkNotSupported(Exception):
    pass


@unique
class EthereumNetwork(Enum):
    """
    Use https://chainlist.org/ as a reference
    """

    UNKNOWN = -1
    OLYMPIC = 0
    MAINNET = 1
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    ETC_KOTTI = 6
    TCH = 7
    UBQ = 8
    OPTIMISTIC = 10
    META = 11
    META_TESTNET = 12
    DIODE_TESTNET = 13
    FLR_FLARE = 14
    DIODE = 15
    FLR_COSTON = 16
    TCH_THAIFI = 17
    TST_TESTNET = 18
    SGB_SONGBIRD = 19
    BOBA_RINKEBY = 28
    RSK = 30
    RSK_TESTNET = 31
    GOOD_TESTNET = 32
    GOOD = 33
    TBWG = 35
    VAL = 38
    TLOS = 40
    TLOS_TESTNET = 41
    KOVAN = 42
    PANGOLIN_FREE_TESTNET = 43
    CRAB_CRAB_NETWORK = 44
    XDC = 50
    TXDC_TESTNET = 51
    CSC = 52
    CSC_TESTNET = 53
    BINANCE = 56
    SYS = 57
    ONTOLOGY = 58
    EOS = 59
    GO = 60
    ELLA = 64
    OKEXCHAIN_TESTNET = 65
    OKEXCHAIN = 66
    DBM_TESTNET = 67
    SOTER = 68
    MIX = 76
    POA_SOKOL = 77
    PC = 78
    GENECHAIN = 80
    METER = 82
    METER_TESTNET = 83
    GTTEST_TESTNET = 85
    GT = 86
    TOMO = 88
    EOS_TESTNET = 95
    BSC_CHAPEL = 97
    POA_CORE = 99
    XDAI = 100
    WEB3GAMES_TESTNET = 102
    VELAS_MAINNET = 106
    TT = 108
    XPR_TESTNET = 110
    ETL = 111
    FUSE_MAINNET = 122
    FUSE_SPARK = 123
    DWU = 124
    FETH_FACTORY127 = 127
    HECO = 128
    MATIC = 137
    DAX = 142
    PHT_SIRIUS = 162
    PHT = 163
    RESIL_TESTNET = 172
    AOX_XDAI = 200
    ENERGY_WEB_CHAIN = 246
    FANTOM = 250
    HECO_TESTNET = 256
    HPB = 269
    BOBA = 288
    KCC_TESTNET = 322
    THETA = 361
    THETA_TESTNET_SAPPHIRE = 363
    THETA_TESTNET_AMBER = 364
    THETA_TESTNET = 365
    CRO = 385
    RUPX = 499
    TAO_CORE = 558
    METIS_TESTNET = 588
    MACA_TESTNET = 595
    KAR = 686
    FETH_FACTORY127_TESTNET = 721
    CHEAPETH_CHEAPNET = 777
    ACA = 787
    HAIC = 803
    WAN = 888
    YETI = 977
    WAN_TESTNET = 999
    KLAY_BAOBAB = 1001
    NEW_TESTNET = 1007
    EURUS_MAINNET = 1008
    EVC_EVRICE = 1010
    NEW = 1012
    SAKURA = 1022
    CLOVER_TESTNET = 1023
    CLOVER = 1024
    METIS = 1088
    MATH = 1139
    MATH_TESTNET = 1140
    MOON_MOONBEAM = 1284
    MOON_MOONRIVER = 1285
    MOON_MOONROCK = 1286
    MOON_MOONBASE = 1287
    MOON_MOONSHADOW = 1288
    GANACHE = 1337
    CATECHAIN = 1618
    RABBIT = 1807
    EURUS_TESTNET = 1984
    EGEM = 1987
    PUBLICMINT_TESTNET = 2019
    PUBLICMINT_MAINNET = 2020
    EDG = 2021
    EDG_BERESHEET = 2022
    KORTHO = 2559
    FANTOM_TESTNET = 4002
    IOTEX_IO = 4689
    IOTEX_IO_TESTNET = 4690
    VENIDIUM_TESTNET = 4918
    VENIDIUM = 4919
    ESN = 5197
    SYS_TESTNET = 5700
    ONTOLOGY_TESTNET = 5851
    RBD = 5869
    SHYFT = 7341
    MDGL_TESTNET = 8029
    GENECHAIN_ADENINE = 8080
    KLAY_CYPRESS = 8217
    KORTHO_TEST = 8285
    OLO = 8723
    OLO_TESTNET = 8724
    BLOXBERG = 8995
    SMARTBCH = 10000
    SMARTBCHTEST_TESTNET = 10001
    GEN = 10101
    SHYFT_TESTNET = 11437
    REI_TESTNET = 12357
    MTT = 16000
    MTTTEST_DEVNET = 16001
    GO_TESTNET = 31337
    FSN = 32659
    NRG = 39797
    ARBITRUM = 42161
    ARBITRUM_NOVA = 42170
    CELO = 42220
    ATH_ATHEREUM = 43110
    AVALANCHE = 43114
    CELO_ALFAJORES = 44787
    REI_MAINNET = 47805
    NRG_TESTNET = 49797
    CELO_BAKLAVA = 62320
    GODWOKEN_TESTNET = 71401
    GODWOKEN = 71402
    VOLTA = 73799
    AKA = 200625
    ARTIS_SIGMA1 = 246529
    ARTIS_TAU1 = 246785
    SPARTA_TESTNET = 333888
    OLYMPUS = 333999
    ARBITRUM_TESTNET = 421611
    ETHO = 1313114
    XERO = 1313500
    MUSIC = 7762959
    MUMBAI = 80001
    PEP_TESTNET = 13371337
    ILT = 18289463
    QKI = 20181205
    AUX = 28945486
    JOYS = 35855456
    AQUA = 61717561
    TOYS_TESTNET = 99415706
    OLT = 311752642
    IPOS = 1122334455
    AURORA = 1313161554
    AURORA_TESTNET = 1313161555
    AURORA_BETANET = 1313161556
    PIRL = 3125659152
    OLT_TESTNET = 4216137055
    PALM_TESTNET = 11297108099
    PALM = 11297108109
    GATHER_DEVNET = 486217935
    GATHER_TESTNET = 356256156
    GATHER_MAINNET = 192837465
    EVMOS_TESTNET = 9000
    EVMOS_MAINNET = 9001
    ASTAR = 592
    SHIDEN = 336
    CRONOS_MAINNET = 25
    CRONOS_TESTNET = 338
    QUARKCHAIN_MAINNET_ROOT = 100000
    QUARKCHAIN_MAINNET_SHARD_0 = 100001
    QUARKCHAIN_MAINNET_SHARD_1 = 100002
    QUARKCHAIN_MAINNET_SHARD_2 = 100003
    QUARKCHAIN_MAINNET_SHARD_3 = 100004
    QUARKCHAIN_MAINNET_SHARD_4 = 100005
    QUARKCHAIN_MAINNET_SHARD_5 = 100006
    QUARKCHAIN_MAINNET_SHARD_6 = 100007
    QUARKCHAIN_MAINNET_SHARD_7 = 100008
    QUARKCHAIN_DEVNET_ROOT = 110000
    QUARKCHAIN_DEVNET_SHARD_0 = 110001
    QUARKCHAIN_DEVNET_SHARD_1 = 110002
    QUARKCHAIN_DEVNET_SHARD_2 = 110003
    QUARKCHAIN_DEVNET_SHARD_3 = 110004
    QUARKCHAIN_DEVNET_SHARD_4 = 110005
    QUARKCHAIN_DEVNET_SHARD_5 = 110006
    QUARKCHAIN_DEVNET_SHARD_6 = 110007
    QUARKCHAIN_DEVNET_SHARD_7 = 110008
    CONFLUX_ESPACE = 1030
    BROCHAIN_MAINNET = 108801
    WAGMI = 11111
    SEPOLIA = 11155111
    IORA_CHAIN = 1197
    SINGULARITY_ZERO_MAINNET = 12052
    POPCATEUM_MAINNET = 1213
    ENTERCHAIN_MAINNET = 1214
    OM_CHAIN_MAINNET = 1246
    OYCHAIN_MAINNET = 126
    HALO_MAINNET = 1280
    PHOENIX_MAINNET = 13381
    SHERPAX_MAINNET = 1506
    BTACHAIN = 1657
    HARMONY_MAINNET_SHARD_0 = 1666600000
    HARMONY_MAINNET_SHARD_1 = 1666600001
    HARMONY_MAINNET_SHARD_2 = 1666600002
    HARMONY_MAINNET_SHARD_3 = 1666600003
    SEELE_MAINNET = 186
    BMC_MAINNET = 188
    NTITY_MAINNET = 197710212030
    BTCIX_NETWORK = 19845
    BITTORRENT_CHAIN_MAINNET = 199
    ELASTOS_SMART_CHAIN = 20
    RANGERS_PROTOCOL_MAINNET = 2025
    DATAHOPPER = 2021121117
    ECOBALL_MAINNET = 2100
    OMCHAIN_MAINNET = 21816
    ELA_DID_SIDECHAIN_MAINNET = 22
    EVANESCO_MAINNET = 2213
    KAVA_EVM = 2222
    DITHEREUM_MAINNET = 24
    NEON_EVM_DEVNET = 245022926
    NEON_EVM_MAINNET = 245022934
    SETHEUM = 258
    EZCHAIN_C_CHAIN_MAINNET = 2612
    SHIBACHAIN = 27
    SOCIAL_SMART_CHAIN_MAINNET = 281121
    GENESIS_L1 = 29
    BITGERT_MAINNET = 32520
    WEB3Q_MAINNET = 333
    PULSECHAIN_MAINNET = 369
    BITTEX_MAINNET = 3690
    SX_NETWORK_MAINNET = 416
    PHI_NETWORK = 4181
    PEGGLECOIN = 42069
    EMERALD_PARATIME_MAINNET = 42262
    AUTOBAHN_NETWORK = 45000
    DOUBLE_A_CHAIN_MAINNET = 512
    UZMI_NETWORK_MAINNET = 5315
    DFK_CHAIN = 53935
    ZYX_MAINNET = 55
    VELA1_CHAIN_MAINNET = 555
    NAHMII_MAINNET = 5551
    REI_CHAIN_MAINNET = 55555
    MOLEREUM_NETWORK = 6022140761023
    ECREDITS_MAINNET = 63000
    PIXIE_CHAIN_MAINNET = 6626
    HOO_SMART_CHAIN = 70
    THINKIUM_MAINNET_CHAIN_0 = 70000
    THINKIUM_MAINNET_CHAIN_1 = 70001
    THINKIUM_MAINNET_CHAIN_2 = 70002
    THINKIUM_MAINNET_CHAIN_103 = 70103
    BLOCKCHAIN_STATION_MAINNET = 707
    IDCHAIN_MAINNET = 74
    RISE_OF_THE_WARBOTS_TESTNET = 7777
    ZENITH_MAINNET = 79
    TELEPORT = 8000
    NOVA_NETWORK = 87
    AMBROS_CHAIN_MAINNET = 880
    VISION_MAINNET = 888888
    GENESIS_COIN = 9100
    ELUVIO_CONTENT_FABRIC = 955305
    GARIZON_STAGE0 = 90
    GARIZON_STAGE1 = 91
    GARIZON_STAGE2 = 92
    GARIZON_STAGE3 = 93
    NEXT_SMART_CHAIN = 96
    LUCKY_NETWORK = 998
    UB_SMART_CHAIN = 99999
    ETHEREUM_CLASSIC_MAINNET = 61
    ETHERINC = 101
    FREIGHT_TRUST_NETWORK = 211
    PERMISSION = 222
    SUR_BLOCKCHAIN_NETWORK = 262
    KCC_MAINNET = 321
    CALLISTO_MAINNET = 820
    WORLD_TRADE_TECHNICAL_BLOCKCHAIN = 1202
    ATHEIOS = 1620
    TESLAFUNDS = 1856
    WEBCHAIN = 24484
    MINTME_COM_COIN = 24734
    ETHERSOCIAL_NETWORK = 31102
    CRYSTALEUM = 103090
    ALAYA_MAINNET = 201018
    PLATON_MAINNET = 210425
    BITTORRENT_CHAIN_TESTNET = 1028
    KAIBA_LIGHTNING_CHAIN_TESTNET = 104
    WEB3GAMES_DEVNET = 105
    NEBULA_TESTNET = 107
    CRYPTOCOINPAY = 10823
    QUADRANS_BLOCKCHAIN = 10946
    QUADRANS_BLOCKCHAIN_TESTNET = 10947
    EVANESCO_TESTNET = 1201
    SINGULARITY_ZERO_TESTNET = 12051
    OYCHAIN_TESTNET = 125
    BOBA_NETWORK_BOBABEAM = 1294
    BOBA_NETWORK_BOBABASE = 1297
    ETND_CHAIN_MAINNETS = 131419
    AITD_MAINNET = 1319
    AITD_TESTNET = 1320
    KINTSUGI = 1337702
    KILN = 1337802
    OPENPIECE_TESTNET = 141
    SHERPAX_TESTNET = 1507
    HARMONY_TESTNET_SHARD_0 = 1666700000
    HARMONY_TESTNET_SHARD_1 = 1666700001
    HARMONY_TESTNET_SHARD_2 = 1666700002
    HARMONY_TESTNET_SHARD_3 = 1666700003
    AIOZ_NETWORK = 168
    LUDAN_MAINNET = 1688
    IVAR_CHAIN_TESTNET = 16888
    HOO_SMART_CHAIN_TESTNET = 170
    AME_CHAIN_MAINNET = 180
    CUBE_CHAIN_MAINNET = 1818
    CUBE_CHAIN_TESTNET = 1819
    BMC_TESTNET = 189
    BON_NETWORK = 1898
    CRYPTO_EMERGENCY = 193
    HARADEV_TESTNET = 197710212031
    MILKOMEDA_C1_MAINNET = 2001
    MILKOMEDA_C1_TESTNET = 200101
    MILKOMEDA_A1_TESTNET = 200202
    CLOUDWALK_MAINNET = 2009
    CLOUDWALK_TESTNET = 2008
    ALAYA_DEV_TESTNET = 201030
    SMARTMESH_MAINNET = 20180430
    TAYCAN_TESTNET = 2023
    ELA_ETH_SIDECHAIN_TESTNET = 21
    ELA_DID_SIDECHAIN_TESTNET = 23
    ECOBALL_TESTNET_ESPUMA = 2101
    CENNZNET_AZALEA = 21337
    FINDORA_MAINNET = 2152
    FINDORA_TESTNET = 2153
    SOTERONE_MAINNET_OLD = 218
    TAYCAN = 22023
    PLATON_DEV_TESTNET = 2203181
    PLATON_DEV_TESTNET2 = 2206132
    KAVA_EVM_TESTNET = 2221
    VCHAIN_MAINNET = 2223
    LACHAIN_MAINNET = 225
    LACHAIN_TESTNET = 226
    HAYMO_TESTNET = 234666
    NEON_EVM_TESTNET = 245022940
    TECHPAY_MAINNET = 2569
    GENESIS_L1_TESTNET = 26
    EZCHAIN_C_CHAIN_TESTNET = 2613
    OASISCHAIN_MAINNET = 26863
    OPTIMISM_ON_GNOSIS_CHAIN = 300
    CENNZNET_RATA = 3000
    CENNZNET_NIKAU = 3001
    PIECE_TESTNET = 30067
    ZCORE_TESTNET = 3331
    WEB3Q_TESTNET = 3333
    WEB3Q_GALILEO = 3334
    DFK_CHAIN_TEST = 335
    DITHEREUM_TESTNET = 34
    PARIBU_NET_MAINNET = 3400
    PARIBU_NET_TESTNET = 3500
    JFIN_CHAIN = 3501
    Q_MAINNET = 35441
    Q_TESTNET = 35443
    DXCHAIN_MAINNET = 36
    CROSSBELL = 3737
    DYNO_MAINNET = 3966
    DYNO_TESTNET = 3967
    YUANCHAIN_MAINNET = 3999
    BOBA_NETWORK_BOBAOPERA_TESTNET = 4051
    AIOZ_NETWORK_TESTNET = 4102
    OPTIMISM_GOERLI_TESTNET = 420
    EMERALD_PARATIME_TESTNET = 42261
    AVALANCHE_FUJI_TESTNET = 43113
    DEXALOT_TESTNET = 432201
    WEELINK_TESTNET = 444900
    DARWINIA_PANGORO_TESTNET = 45
    DARWINIA_NETWORK = 46
    OPENCHAIN_MAINNET = 474142
    CMP_TESTNET = 512512
    DOUBLE_A_CHAIN_TESTNET = 513
    TLCHAIN_NETWORK_MAINNET = 5177
    XT_SMART_CHAIN_MAINNET = 520
    F_X_CORE_MAINNET_NETWORK = 530
    CANDLE = 534
    OPENPIECE_MAINNET = 54
    NAHMII_TESTNET = 5553
    REI_CHAIN_TESTNET = 55556
    DIGEST_SWARM_CHAIN = 5777
    KARURA_NETWORK_TESTNET = 596
    ACALA_NETWORK_TESTNET = 597
    MESHNYAN_TESTNET = 600
    THINKIUM_TESTNET_CHAIN_0 = 60000
    THINKIUM_TESTNET_CHAIN_1 = 60001
    THINKIUM_TESTNET_CHAIN_103 = 60103
    THINKIUM_TESTNET_CHAIN_2 = 60002
    ETHEREUM_CLASSIC_TESTNET_MORDEN = 62
    ETHEREUM_CLASSIC_TESTNET_MORDOR = 63
    MULTIVAC_MAINNET = 62621
    ECREDITS_TESTNET = 63001
    SX_NETWORK_TESTNET = 647
    PIXIE_CHAIN_TESTNET = 666
    VISION_VPIONEER_TEST_CHAIN = 666666
    OPTIMISM_KOVAN = 69
    CONDRIEU = 69420
    TOMB_CHAIN_MAINNET = 6969
    STAR_SOCIAL_TESTNET = 700
    ELLA_THE_HEART = 7027
    BLOCKCHAIN_STATION_TESTNET = 708
    CONFLUX_ESPACE_TESTNET = 71
    POLYJUICE_TESTNET = 71393
    DXCHAIN_TESTNET = 72
    MIXIN_VIRTUAL_MACHINE = 73927
    OPENCHAIN_TESTNET = 776
    FIRENZE_TEST_NETWORK = 78110
    HAZLOR_TESTNET = 7878
    AEROCHAIN_TESTNET = 788
    PORTAL_FANTASY_CHAIN_TEST = 808
    ZENITH_TESTNET_VILNIUS = 81
    CALLISTO_TESTNET = 821
    GODWOKEN_TESTNET_V1 = 868455272153094
    AMBROS_CHAIN_TESTNET = 8888
    IVAR_CHAIN_MAINNET = 88888
    MAMMOTH_MAINNET = 8898
    TOMOCHAIN_TESTNET = 89
    UBIQ_NETWORK_TESTNET = 9
    GARIZON_TESTNET_STAGE0 = 900
    GARIZON_TESTNET_STAGE1 = 901
    GARIZON_TESTNET_STAGE2 = 902
    GARIZON_TESTNET_STAGE3 = 903
    BERYLBIT_MAINNET = 9012
    PORTAL_FANTASY_CHAIN = 909
    PULSECHAIN_TESTNET = 940
    PULSECHAIN_TESTNET_V2B = 941
    PULSECHAIN_TESTNET_V3 = 942
    RANGERS_PROTOCOL_TESTNET_ROBIN = 9527
    TOP_MAINNET_EVM = 980
    TOP_MAINNET = 989
    MYOWN_TESTNET = 9999
    UB_SMART_CHAIN_TESTNET = 99998

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN
