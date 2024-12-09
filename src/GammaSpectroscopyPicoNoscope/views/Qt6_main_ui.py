# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt6_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 764)
        self.actionExport_spectrum = QAction(MainWindow)
        self.actionExport_spectrum.setObjectName(u"actionExport_spectrum")
        self.actionWrite_output_files = QAction(MainWindow)
        self.actionWrite_output_files.setObjectName(u"actionWrite_output_files")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_tabs = QTabWidget(self.centralwidget)
        self.plot_tabs.setObjectName(u"plot_tabs")
        self.event_tab = QWidget()
        self.event_tab.setObjectName(u"event_tab")
        self.verticalLayout_2 = QVBoxLayout(self.event_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.event_plot = PlotWidget(self.event_tab)
        self.event_plot.setObjectName(u"event_plot")

        self.verticalLayout_2.addWidget(self.event_plot)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.reset_event_axes_button = QPushButton(self.event_tab)
        self.reset_event_axes_button.setObjectName(u"reset_event_axes_button")

        self.horizontalLayout_3.addWidget(self.reset_event_axes_button)

        self.toggle_guides_button1 = QPushButton(self.event_tab)
        self.toggle_guides_button1.setObjectName(u"toggle_guides_button1")

        self.horizontalLayout_3.addWidget(self.toggle_guides_button1)

        self.toggle_markslines_button1 = QPushButton(self.event_tab)
        self.toggle_markslines_button1.setObjectName(u"toggle_markslines_button1")

        self.horizontalLayout_3.addWidget(self.toggle_markslines_button1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.plot_tabs.addTab(self.event_tab, "")
        self.spectrum_tab = QWidget()
        self.spectrum_tab.setObjectName(u"spectrum_tab")
        self.verticalLayout_3 = QVBoxLayout(self.spectrum_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.spectrum_plot = PlotWidget(self.spectrum_tab)
        self.spectrum_plot.setObjectName(u"spectrum_plot")

        self.verticalLayout_3.addWidget(self.spectrum_plot)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.reset_spectrum_axes_button = QPushButton(self.spectrum_tab)
        self.reset_spectrum_axes_button.setObjectName(u"reset_spectrum_axes_button")

        self.horizontalLayout_6.addWidget(self.reset_spectrum_axes_button)

        self.toggle_guides_button2 = QPushButton(self.spectrum_tab)
        self.toggle_guides_button2.setObjectName(u"toggle_guides_button2")

        self.horizontalLayout_6.addWidget(self.toggle_guides_button2)

        self.toggle_markslines_button2 = QPushButton(self.spectrum_tab)
        self.toggle_markslines_button2.setObjectName(u"toggle_markslines_button2")

        self.horizontalLayout_6.addWidget(self.toggle_markslines_button2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.plot_tabs.addTab(self.spectrum_tab, "")

        self.verticalLayout.addWidget(self.plot_tabs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clear_run_button = QPushButton(self.centralwidget)
        self.clear_run_button.setObjectName(u"clear_run_button")

        self.horizontalLayout.addWidget(self.clear_run_button)

        self.single_button = QPushButton(self.centralwidget)
        self.single_button.setObjectName(u"single_button")

        self.horizontalLayout.addWidget(self.single_button)

        self.run_stop_button = QPushButton(self.centralwidget)
        self.run_stop_button.setObjectName(u"run_stop_button")

        self.horizontalLayout.addWidget(self.run_stop_button)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout.addWidget(self.label_24)

        self.run_number_label = QLabel(self.centralwidget)
        self.run_number_label.setObjectName(u"run_number_label")
        self.run_number_label.setMinimumSize(QSize(30, 0))
        self.run_number_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.run_number_label.setMargin(0)

        self.horizontalLayout.addWidget(self.run_number_label)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.run_time_label = QLabel(self.centralwidget)
        self.run_time_label.setObjectName(u"run_time_label")
        self.run_time_label.setMinimumSize(QSize(40, 0))
        self.run_time_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.run_time_label.setMargin(0)

        self.horizontalLayout.addWidget(self.run_time_label)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.measuring_time_label = QLabel(self.centralwidget)
        self.measuring_time_label.setObjectName(u"measuring_time_label")
        self.measuring_time_label.setMinimumSize(QSize(40, 0))
        self.measuring_time_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.measuring_time_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.measuring_time_label)

        self.num_events_label = QLabel(self.centralwidget)
        self.num_events_label.setObjectName(u"num_events_label")

        self.horizontalLayout.addWidget(self.num_events_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.range_box = QComboBox(self.centralwidget)
        self.range_box.setObjectName(u"range_box")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.range_box)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.offset_box = QDoubleSpinBox(self.centralwidget)
        self.offset_box.setObjectName(u"offset_box")
        self.offset_box.setDecimals(0)
        self.offset_box.setMinimum(-100.000000000000000)
        self.offset_box.setMaximum(100.000000000000000)
        self.offset_box.setValue(0.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.offset_box)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.threshold_box = QDoubleSpinBox(self.centralwidget)
        self.threshold_box.setObjectName(u"threshold_box")
        self.threshold_box.setDecimals(3)
        self.threshold_box.setMinimum(-40.000000000000000)
        self.threshold_box.setMaximum(40.000000000000000)
        self.threshold_box.setSingleStep(0.010000000000000)
        self.threshold_box.setValue(0.010000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.threshold_box)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.trigger_box = QCheckBox(self.centralwidget)
        self.trigger_box.setObjectName(u"trigger_box")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.trigger_box)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_16)

        self.trigger_channel_box = QComboBox(self.centralwidget)
        self.trigger_channel_box.addItem("")
        self.trigger_channel_box.addItem("")
        self.trigger_channel_box.addItem("")
        self.trigger_channel_box.setObjectName(u"trigger_channel_box")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.trigger_channel_box)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.coupling_box = QComboBox(self.centralwidget)
        self.coupling_box.setObjectName(u"coupling_box")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.coupling_box)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_15)

        self.polarity_box = QComboBox(self.centralwidget)
        self.polarity_box.setObjectName(u"polarity_box")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.polarity_box)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.timebase_box = QSpinBox(self.centralwidget)
        self.timebase_box.setObjectName(u"timebase_box")
        self.timebase_box.setMinimum(2)
        self.timebase_box.setMaximum(65535)
        self.timebase_box.setValue(20)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.timebase_box)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_8)

        self.sampling_time_label = QLabel(self.centralwidget)
        self.sampling_time_label.setObjectName(u"sampling_time_label")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.sampling_time_label)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_5)

        self.pre_trigger_box = QDoubleSpinBox(self.centralwidget)
        self.pre_trigger_box.setObjectName(u"pre_trigger_box")
        self.pre_trigger_box.setDecimals(3)
        self.pre_trigger_box.setMaximum(100000.000000000000000)
        self.pre_trigger_box.setValue(10.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.pre_trigger_box)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_6)

        self.post_trigger_box = QDoubleSpinBox(self.centralwidget)
        self.post_trigger_box.setObjectName(u"post_trigger_box")
        self.post_trigger_box.setDecimals(3)
        self.post_trigger_box.setMaximum(1000000.000000000000000)
        self.post_trigger_box.setValue(10.000000000000000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.post_trigger_box)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_9)

        self.num_samples_label = QLabel(self.centralwidget)
        self.num_samples_label.setObjectName(u"num_samples_label")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.num_samples_label)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_13)

        self.num_captures_box = QSpinBox(self.centralwidget)
        self.num_captures_box.setObjectName(u"num_captures_box")
        self.num_captures_box.setMinimum(1)
        self.num_captures_box.setMaximum(10000)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.num_captures_box)

        self.label_161 = QLabel(self.centralwidget)
        self.label_161.setObjectName(u"label_161")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_161)

        self.baseline_correction_box = QCheckBox(self.centralwidget)
        self.baseline_correction_box.setObjectName(u"baseline_correction_box")
        self.baseline_correction_box.setChecked(True)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.baseline_correction_box)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_18)

        self.ch_A_enabled_box = QCheckBox(self.centralwidget)
        self.ch_A_enabled_box.setObjectName(u"ch_A_enabled_box")
        self.ch_A_enabled_box.setChecked(True)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.ch_A_enabled_box)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_19)

        self.ch_B_enabled_box = QCheckBox(self.centralwidget)
        self.ch_B_enabled_box.setObjectName(u"ch_B_enabled_box")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.ch_B_enabled_box)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_20)

        self.lld_box = QDoubleSpinBox(self.centralwidget)
        self.lld_box.setObjectName(u"lld_box")
        self.lld_box.setDecimals(1)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.lld_box)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_21)

        self.uld_box = QDoubleSpinBox(self.centralwidget)
        self.uld_box.setObjectName(u"uld_box")
        self.uld_box.setDecimals(1)
        self.uld_box.setValue(100.000000000000000)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.uld_box)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_22)

        self.num_bins_box = QSpinBox(self.centralwidget)
        self.num_bins_box.setObjectName(u"num_bins_box")
        self.num_bins_box.setMaximum(4095)
        self.num_bins_box.setValue(256)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.num_bins_box)

        self.upper_trigger_box = QCheckBox(self.centralwidget)
        self.upper_trigger_box.setObjectName(u"upper_trigger_box")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.upper_trigger_box)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_23)

        self.upper_threshold_box = QDoubleSpinBox(self.centralwidget)
        self.upper_threshold_box.setObjectName(u"upper_threshold_box")
        self.upper_threshold_box.setDecimals(3)
        self.upper_threshold_box.setMinimum(-40.000000000000000)
        self.upper_threshold_box.setMaximum(40.000000000000000)
        self.upper_threshold_box.setSingleStep(0.010000000000000)
        self.upper_threshold_box.setValue(1.000000000000000)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.upper_threshold_box)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_10)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.run_duration_box = QSpinBox(self.centralwidget)
        self.run_duration_box.setObjectName(u"run_duration_box")
        self.run_duration_box.setMinimum(1)
        self.run_duration_box.setMaximum(1000000)
        self.run_duration_box.setValue(600)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.run_duration_box)


        self.verticalLayout_4.addLayout(self.formLayout_6)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExport_spectrum)
        self.menuFile.addAction(self.actionWrite_output_files)

        self.retranslateUi(MainWindow)

        self.plot_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gamma Spectroscopy Qt6", None))
        self.actionExport_spectrum.setText(QCoreApplication.translate("MainWindow", u"Export spectrum", None))
#if QT_CONFIG(shortcut)
        self.actionExport_spectrum.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionWrite_output_files.setText(QCoreApplication.translate("MainWindow", u"Write output files", None))
#if QT_CONFIG(shortcut)
        self.actionWrite_output_files.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.reset_event_axes_button.setText(QCoreApplication.translate("MainWindow", u"Reset axes", None))
        self.toggle_guides_button1.setText(QCoreApplication.translate("MainWindow", u"Toggle guides", None))
        self.toggle_markslines_button1.setText(QCoreApplication.translate("MainWindow", u"Toggle marks/lines", None))
        self.plot_tabs.setTabText(self.plot_tabs.indexOf(self.event_tab), QCoreApplication.translate("MainWindow", u"Event plot", None))
        self.reset_spectrum_axes_button.setText(QCoreApplication.translate("MainWindow", u"Reset axes", None))
        self.toggle_guides_button2.setText(QCoreApplication.translate("MainWindow", u"Toggle guides", None))
        self.toggle_markslines_button2.setText(QCoreApplication.translate("MainWindow", u"Toggle marks/lines", None))
        self.plot_tabs.setTabText(self.plot_tabs.indexOf(self.spectrum_tab), QCoreApplication.translate("MainWindow", u"Spectrum plot", None))
        self.clear_run_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.single_button.setText(QCoreApplication.translate("MainWindow", u"Single", None))
        self.run_stop_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Run:", None))
        self.run_number_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Run time:", None))
        self.run_time_label.setText(QCoreApplication.translate("MainWindow", u"0 s", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Measuring time: ", None))
        self.measuring_time_label.setText(QCoreApplication.translate("MainWindow", u"0 s", None))
        self.num_events_label.setText(QCoreApplication.translate("MainWindow", u"(0 events)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Range:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.offset_box.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Trigger threshold:", None))
        self.threshold_box.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enable trigger:", None))
        self.trigger_box.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Trigger on:", None))
        self.trigger_channel_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Channel A", None))
        self.trigger_channel_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Channel B", None))
        self.trigger_channel_box.setItemText(2, QCoreApplication.translate("MainWindow", u"A OR B", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Coupling:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pulse polarity:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Timebase:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sampling time:", None))
        self.sampling_time_label.setText(QCoreApplication.translate("MainWindow", u"0 \u03bcs", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pre-trigger window:", None))
        self.pre_trigger_box.setSuffix(QCoreApplication.translate("MainWindow", u" \u03bcs", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Post-trigger window:", None))
        self.post_trigger_box.setSuffix(QCoreApplication.translate("MainWindow", u" \u03bcs", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Number of samples:", None))
        self.num_samples_label.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Number of captures:", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Baseline correction:", None))
        self.baseline_correction_box.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Show channel A:", None))
        self.ch_A_enabled_box.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Show channel B:", None))
        self.ch_B_enabled_box.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Lower level discriminator:", None))
        self.lld_box.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Upper level discriminator:", None))
        self.uld_box.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Histogram bins:", None))
        self.upper_trigger_box.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Enable upper threshold", None))
        self.upper_threshold_box.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Upper threshold (SW):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Run duration:", None))
        self.run_duration_box.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

