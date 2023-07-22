_base_ = [
    '../../../_base_/datasets/nway_kshot/few_shot_voc_ms.py',
    '../../../_base_/schedules/schedule.py', '../../vfa_r101_c4.py',
    '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        save_dataset=True,
        dataset=dict(
            type='FewShotVOCDefaultDataset',
            ann_cfg=[dict(method='MetaRCNN', setting='SPLIT1_10SHOT')],
            num_novel_shots=10,
            num_base_shots=10,
            classes='ALL_CLASSES_SPLIT1',
        )),
    val=dict(classes='ALL_CLASSES_SPLIT1'),
    test=dict(classes='ALL_CLASSES_SPLIT1'),
    model_init=dict(classes='ALL_CLASSES_SPLIT1'))
evaluation = dict(
    interval=2000, class_splits=['BASE_CLASSES_SPLIT1', 'NOVEL_CLASSES_SPLIT1'])
checkpoint_config = dict(interval=2000)
optimizer = dict(lr=0.001)
lr_config = dict(warmup=None)
runner = dict(max_iters=2000)
load_from = 'work_dirs/vfa_r101_c4_8xb4_voc-split1_base-training/iter_18000.pth'

# model settings
model = dict(frozen_parameters=[
    'backbone', 'shared_head',  'aggregation_layer',  'rpn_head',
])