from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QToolButton


def create_action(parent,
                  text,
                  shortcut=None,
                  icon=None,
                  tip=None,
                  toggled=None,
                  triggered=None,
                  data=None,
                  menurole=None,
                  context=Qt.WindowShortcut):

    """Create a QAction"""
    action = QAction(text, parent)

    if triggered is not None:
        action.triggered.connect(triggered)

    if toggled is not None:
        action.toggled.connect(toggled)
        action.setCheckable(True)

    # if icon is not None:
    #     if is_text_string(icon):
    #         icon = get_icon(icon)
    #     action.setIcon(icon)

    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)

    if data is not None:
        action.setData(data)

    if menurole is not None:
        action.setMenuRole(menurole)

    if shortcut is not None:
        action.setShortcut(shortcut)
        action.setShortcutContext(context)

    return action

def create_toolbutton(parent,
                      text=None,
                      shortcut=None,
                      icon=None,
                      tip=None,
                      toggled=None,
                      triggered=None,
                      autoraise=True,
                      text_beside_icon=False):

    """Create a QToolButton"""
    button = QToolButton(parent)
    if text is not None:
        button.setText(text)
    # if icon is not None:
    #     if is_text_string(icon):
    #         icon = get_icon(icon)
    #     button.setIcon(icon)
    if text is not None or tip is not None:
        button.setToolTip(text if tip is None else tip)
    if text_beside_icon:
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    button.setAutoRaise(autoraise)
    if triggered is not None:
        button.clicked.connect(triggered)
    if toggled is not None:
        button.toggled.connect(toggled)
        button.setCheckable(True)
    if shortcut is not None:
        button.setShortcut(shortcut)
    return button


# def add_actions(target, actions, insert_before=None):
#     """Add actions to a QMenu or a QToolBar."""
#     previous_action = None
#     target_actions = list(target.actions())
#     if target_actions:
#         previous_action = target_actions[-1]
#         if previous_action.isSeparator():
#             previous_action = None
#     for action in actions:
#         if (action is None) and (previous_action is not None):
#             if insert_before is None:
#                 target.addSeparator()
#             else:
#                 target.insertSeparator(insert_before)
#         elif isinstance(action, QMenu):
#             if insert_before is None:
#                 target.addMenu(action)
#             else:
#                 target.insertMenu(insert_before, action)
#         elif isinstance(action, QAction):
#             if isinstance(action, SpyderAction):
#                 if isinstance(target, QMenu) or not isinstance(target, QToolBar):
#                     action = action.no_icon_action
#             if insert_before is None:
#                 target.addAction(action)
#             else:
#                 target.insertAction(insert_before, action)
#         previous_action = action