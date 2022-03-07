from pcdirector import PcDirector

if __name__ == '__main__':
    pc_maker = PcDirector()
    pc_maker.construct_pc('64GB', '256GB', 'NVIDIA super128')

    print(pc_maker.computer)