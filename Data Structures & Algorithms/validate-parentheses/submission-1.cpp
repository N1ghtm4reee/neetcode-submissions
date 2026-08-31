class Solution {
public:
    bool isValid(string s) {
        stack<char> _stack;
        int size = s.size();
        for (int i = 0; i < size; i++) {
            if (s[i] == '[' || s[i] == '{' || s[i] == '(') {
                _stack.push(s[i]);
            }
            else if (_stack.size() > 0){
                if (s[i] == ']' && _stack.top() == '[')
                    _stack.pop();
                else if (s[i] == ')' && _stack.top() == '(')
                    _stack.pop();
                else if (s[i] == '}' && _stack.top() == '{')
                    _stack.pop();
                else
                    return false;
            }
            else
                return false;
        }
        return _stack.size() > 0 ? false : true;
    }
};
