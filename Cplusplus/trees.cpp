#include <iostream>

#define DEBUG

using namespace std;

class Node {
    int key;
    Node* left;
    Node* right;
    
public:
    Node() {
        key   = -1;
        left  = NULL;
        right = NULL;
    };
    
    void setKey(int value)      { key   = value; };
    void setLeft(Node *aLeft)   { left  = aLeft; };
    void setRight(Node *aRight) { right = aRight; };
    int Key()     { return key; };
    Node* Left()  { return left; };
    Node* Right() { return right; };
};

class Tree {
    Node* root;
public:
    Tree();
    ~Tree();
    Node *Root() { return root; };
    void addNode(int key);
    void inOrder(Node* n);
    void preOrder(Node* n);
    void postOrder(Node* n);
private:
    void addNode(int key, Node* leaf);
    void freeNode(Node* leaf);
    void printKey(Node* n);
};

Tree::Tree() { root = NULL; }
Tree::~Tree() { freeNode(root); }

void Tree::freeNode(Node* leaf) {
    if (leaf != NULL) {
        freeNode(leaf->Left());
        freeNode(leaf->Right());
        delete leaf;
    }
}

// public
void Tree::addNode(int key) {
    if (root == NULL) {
        #ifdef DEBUG
        cout << "add root node ... " << key << endl;
        #endif
        Node* n = new Node();
        n->setKey(key);
        root = n;
    } else {
        #ifdef DEBUG
        cout << "add other node ... " << key << endl;
        #endif
        addNode(key, root);
    }
}

// private
void Tree::addNode(int key, Node *leaf) {
    if (key <= leaf->Key()) {
        if (leaf->Left() != NULL)
            addNode(key, leaf->Left());
        else {
            Node* n = new Node();
            n->setKey(key);
            leaf->setLeft(n);
        }    
    } else {
        if (leaf->Right() != NULL)
            addNode(key, leaf->Right());
        else {
            Node* n = new Node();
            n->setKey(key);
            leaf->setRight(n);   
        }
    }
}

void Tree::printKey(Node* n) {
    #ifdef DEBUG
    cout << n->Key() << " ";
    #endif
}

void Tree::inOrder(Node* n) {
    if (n) {
        inOrder(n->Left());
        printKey(n);     
        inOrder(n->Right());
    }
}

void Tree::preOrder(Node* n) {
    if (n) {
        printKey(n);  
        preOrder(n->Left());   
        preOrder(n->Right());
    }
}

void Tree::postOrder(Node* n) {
    if (n) { 
        postOrder(n->Left());   
        postOrder(n->Right());
        printKey(n); 
    }
}

int main() {
    Tree* tree = new Tree();
    tree->addNode(8);
    tree->addNode(3);
    tree->addNode(10);
    tree->addNode(1);
    tree->addNode(6);
    tree->addNode(4);
    tree->addNode(7);
    tree->addNode(14);
    tree->addNode(13);
    tree->addNode(15);
    tree->addNode(9);
    
    /******************
    
    Our tree should be:
            8
         /    \    
       3        10
      / \      /  \ 
     1   6    9    14
        / \        / \
        4 7      13  15  
    ***********************/
    
    // output should be: 1 3 4 6 7 8 9 10 13 14 15
    cout << "In-order traversal" << endl;
    tree->inOrder(tree->Root());
    cout << endl;
    
    // output should be: 8 3 1 6 4 7 10 9 14 13 15
    cout << "Pre-order traversal" << endl;
    tree->preOrder(tree->Root());
    cout << endl;
    
    // output should be: 1 47 6 3 9 13 15 14 10 8
    cout << "Post-order traversal" << endl;
    tree->postOrder(tree->Root());
    cout << endl;
    
    delete tree;
    return 0;   
}
