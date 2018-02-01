def main():
    memory_type_strings = ['TMM Memory Used', 'Other Memory Used', 'Swap Used']
    structured_data = {}
    chunked_sections = None
    with open('memory_1_31_18', 'r') as f_hdl:
        chunked_sections = f_hdl.read().split('\n\n')
    split_memory_section = chunked_sections[0].split('\n')
    for line in split_memory_section:
        for memory_type in memory_type_strings:
            if memory_type in line:
                raw_split_stats = line[len(memory_type):].split(' ')
                filtered_raw_split_stats = list(filter(lambda x: x != '', raw_split_stats))
                structured_data[memory_type] = (filtered_raw_split_stats[0], filtered_raw_split_stats[1], filtered_raw_split_stats[2])
                break
    print(structured_data)


if __name__ == '__main__':
    main()
