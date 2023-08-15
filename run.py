

def get_dict_paths(in_dict):
    '''
    非递归方法，深度优先获得所有的从根节点到叶子节点的路径以及叶子节点的值
    '''
    root_name='root'
    in_dict={root_name:in_dict}
    def get_child(nodes):
        d=in_dict
        for node in nodes:
            d=d[node]
        return (d,node)
    if not in_dict[root_name]:
        return []
    stack=[get_child([root_name])]
    paths=[[root_name]]
    leaf_value=[]
    current_index=0
    #pre_order=[]
    while stack:
        p,node_name=stack.pop()
        #pre_order.append(node_name)
        if isinstance(p, dict):
            p_keys=list(p.keys())
        else:
            leaf_value.append(p)
            current_index-=1
            continue
        current_path=paths[current_index].copy()
        indexs=[index for (index,value) in enumerate(paths) if value == current_path]
        diff = len(p_keys)-len(indexs)
        last_index=indexs[-1]
        if diff>0:
            for i in range(1,diff+1):
                pos = last_index+i
                indexs.append(pos)
                tmp = current_path.copy()
                tmp.append(p_keys[i])
                paths.insert(pos,tmp)
        paths[indexs[0]].append(p_keys[0])
        for i in indexs:
            stack.append(get_child(paths[i]))
        current_index=indexs[-1]
    leaf_value.reverse()        
    return [path[1:] for path in paths],leaf_value

if __name__ == '__main__':
    category={'vertical_door':0,'horizontal_door':0,'window':0,'electrical_door':0,'elevator':0,'unknown':0}
    state={'half_open':0,'open':0,'close':0,'unknown':0}
    statistics={'label':
                    {
                    'precision':
                        {
                            'wun':
                            {
                                'category':category.copy(),
                                'state':state.copy()
                            },
                            'woun':
                            {
                                'category':category.copy(),
                                'state':state.copy()
                            }
                        },
                    'recall':
                        {
                            'wun':
                            {
                                'category':category.copy(),
                                'state':state.copy()
                            },
                            'woun':
                            {
                                'category':category.copy(),
                                'state':state.copy()
                            }
                        }
                    }
                    ,
                    'bbox':
                    {
                        'precision':
                        {
                            'wun':
                            {
                                'bbox':0.0,
                                'category':category.copy(),
                                'state':state.copy()
                            },
                            'woun':
                            {
                                'bbox':0.0,
                                'category':category.copy(),
                                'state':state.copy()
                            }
                        },
                        'recall':
                        {
                            'wun':
                            {
                                'bbox':0.0,
                                'category':category.copy(),
                                'state':state.copy()
                            },
                            'woun':
                            {
                                'bbox':0.0,
                                'category':category.copy(),
                                'state':state.copy()
                            }
    
                        }
                    }
                    }
    import time
    start = time.time()
    rst = get_dict_paths(statistics)
    end = time.time()
    print("time-cost: {:.8f}s".format(end - start))
