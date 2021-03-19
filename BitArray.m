classdef BitArray
    properties
        arr;
        size;
    end
    methods
        function obj = BitArray(size)
            obj.size = size;
            obj.arr = containers.Map;
            for i = 1:size
                obj.arr(int2str(i)) = 0;
            end
        end
        function set(obj, i, val)
            obj.arr(int2str(i)) = val;
        end
        function val = get(obj, i)
            val = obj.arr(int2str(i));
        end
    end
end