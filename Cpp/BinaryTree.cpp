#include <iostream>
#include <queue>
#include <stack>
using namespace std;

struct TreeNode {
    char data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(char val) : data(val), left(nullptr), right(nullptr) {}
};

void reverseLevelOrder(TreeNode* root) {
    if (root == nullptr) return;

    queue<TreeNode*> q;
    stack<TreeNode*> s;

    q.push(root);

    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();

        s.push(current);

        if (current->right) q.push(current->right);
        if (current->left) q.push(current->left);
    }

    while (!s.empty()) {
        cout << s.top()->data << " ";
        s.pop();
    }
    cout << endl;
}

TreeNode* buildTree() {
    TreeNode* root = new TreeNode('A');
    root->left = new TreeNode('B');
    root->right = new TreeNode('C');
    root->left->left = new TreeNode('D');
    root->left->right = new TreeNode('E');
    root->right->left = new TreeNode('F');
    root->right->right = new TreeNode('G');
    root->left->left->left = new TreeNode('H');
    return root;
}

int main() {
    TreeNode* root = buildTree();
    cout << "Reverse Level Order Traversal: ";
    reverseLevelOrder(root);
    return 0;
}
