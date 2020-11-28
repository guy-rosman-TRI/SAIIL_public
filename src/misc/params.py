import argparse

def parse_arguments(default_modelname='visual_models.pt',default_temporal_modelname='temporal_models.pt',default_dataset_type='multidict',additional_setters=[]):
    # TODO(guy.rosman): add help
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, conflict_handler='resolve')
    parser.add_argument('--show_samples', action='store_true', help="")
    parser.add_argument('--data_dir', action='store', default="~/data_mgh/AI Sleeve Videos/", help="Data folder")
    parser.add_argument('--log_dir', action='store', default="./logs/", help="Data folder")
    parser.add_argument('--cache_dir', action='store', default="~/cache_mgh", help="Cache dir for datasets")

    parser.add_argument('--annotation_filename', action='store', default='Updated Annotations Sleeve.ods', help="")
    parser.add_argument('--results_filename', action='store', default='results.pkl', help="")
    parser.add_argument('--model_filename', action='store', default=default_modelname, help="")
    parser.add_argument('--temporal_model_filename', action='store', default=default_temporal_modelname, help="")
    parser.add_argument('--dataset_type', action='store', default=default_dataset_type, help="")
    parser.add_argument('--output_filename', action='store', default="output.pkl", help="")
    parser.add_argument('--num_epochs', action='store', type=int, default=100, help="")
    parser.add_argument('--confusion_matrix_samples', action='store', type=int, default=10000, help="")
    parser.add_argument('--learning_rate', action='store', type=float, default=0.001, help="")
    # The amount of samples to take from the data, as a float, or a point to a json that matches phase to fraction.
    parser.add_argument('--fractions', action='store', default=1.0, help="")
    parser.add_argument('--min_seg_fraction', action='store', type=float, default=0.99999, help="")
    parser.add_argument('--max_seg_fraction', action='store', type=float, default=1.0, help="")
    parser.add_argument('--training_ratio', action='store', type=float, default=0.7, help="")
    parser.add_argument('--segment_ratio', action='store', type=float, default=1.0, help="")
    parser.add_argument('--sampling_step', action='store', type=int, default=50, help="")
    parser.add_argument('--temporal_length', action='store', type=int, default=8, help="")
    parser.add_argument('--num_dataloader_workers', action='store', type=int, default=4, help="")
    parser.add_argument('--saving_step', action='store', type=int, default=10, help="")
    parser.add_argument('--batch_size', action='store', type=int, default=64, help="")
    parser.add_argument('--image_width', action='store', type=int, default=224, help="")
    parser.add_argument('--image_height', action='store', type=int, default=224, help="")
    parser.add_argument('--epoch_size', action='store', type=int, default=2048, help="epoch size")
    parser.add_argument('--epoch_size_phase_id', action='store', type=int, default=10240, help="epoch size")
    parser.add_argument('--epoch_size_gan', action='store', type=int, default=128, help="epoch size")
    parser.add_argument('--num_training_experiments', action='store', type=int, default=1, help="number of training experiments/repetitions")
    parser.add_argument('--disable_cuda', action='store', type=bool, default=False, help="should disable cuda")
    parser.add_argument('--cuda_device', action='store', type=str, default="0", help="cuda device index: 0 or 1")
    # JSON file to map phase names
    parser.add_argument('--phase_translation_file', action='store', default=None, help="")

    # map from Video ID to Redcap ID
    parser.add_argument('--video_redcap_translation_file', action='store', default='', help="")
    parser.add_argument('--video_redcap_data_file', action='store', default='', help="")
    parser.add_argument('--video_surgeon_translation_file', action='store', default='', help="")
    # A str of (gt_label)_(pred_label) denoting which examples to view, e.g. '1,2'. If set to 'errors', view all examples that are
    # mislabeled in the confusion matrix. If 'all', sample all examples (need to add)
    parser.add_argument('--view_examples', action='store', type=str, default='all')
    # How to show examples. Options include:
    # * image - show the frame and video filename, time in the video
    # * text - write a list of examples as a text format (TBD; consider: json?)
    parser.add_argument('--view_type', action='store', type=str, default='image')
    parser.add_argument('--pre_train_temporal_model_filename', action='store', default=None, help="")
    parser.add_argument('--pre_train_visual_model_filename', action='store', default=None, help="")
    parser.add_argument('--load_pretrained_model', action='store_true', default=None, help="")
    parser.add_argument('--sampling_rate', action='store', type=float, default=5, help="")      # unit frame per second (fps)
    parser.add_argument('--phase_order_filename', action='store', default=None, help="")
    parser.add_argument('--phase_transition_filename', action='store', default=None, help="")
    parser.add_argument('--phase_length_filename', action='store', default=None, help="")
    parser.add_argument('--video_name_list_filename', action='store', default=None, help="")
    parser.add_argument('--training_filename', action='store', default=None, help="")
    parser.add_argument('--inference_filename', action='store', default=None, help="")
    parser.add_argument('--plot_save_dir', action='store', default=None, help="")
    parser.add_argument('--ssm_dropout_ratio', action='store', type=float, default=0.33, help="")
    parser.add_argument('--visual_dropout_ratio', action='store', type=float, default=0.33, help="")
    parser.add_argument('--img_loss_coefficient', action='store', type=float, default=0.0, help="")
    parser.add_argument('--regressor_beta_distribution', action='store', type=bool, default=False, help="progress regression beta distribution")
    parser.add_argument('--multitask_list', '--list', action='append', default=[], help='e.g. progress_regressor or img_reconstruction', required=False)
    parser.add_argument('--lstm_size', action='store', type=int, default=64, help="")
    parser.add_argument('--plot_fingerprints', action='store', type=bool, default=False, help="should plot results")
    parser.add_argument('--plot_confusion_matrix', action='store', type=bool, default=False, help="should plot confusion matrix")
    parser.add_argument('--plot_video', action='store', type=bool, default=False, help="should plot video")
    parser.add_argument('--write_txt_results', action='store', type=bool, default=True, help="should plot results")
    parser.add_argument('--use_temporal_cnn', action='store_true', help="should use temporal cnn instead of lstm")
    parser.add_argument('--skip_full_forward', action='store_true', help="Do not run the full forward inference, use zeros")
    parser.add_argument('--gan_simulate_data_filename', action='store', default=None, help="the simulated data json file name")
    parser.add_argument('--phase_pretrain_iter', action='store', type=int, default=100, help="")
    parser.add_argument('--data_pretraining_iter', action='store', type=int, default=30, help="")
    parser.add_argument('--gan_training_iter', action='store', type=int, default=2000, help="")
    parser.add_argument('--past_emr_column_names', action='store', type=str, default='', help="json w/ column names for past variables from emr")
    parser.add_argument('--future_emr_column_names', action='store', type=str, default='', help="json w/ column names for future variables from emr")
    parser.add_argument('--gan_past_length', action='store', type=int, default=10, help="")
    parser.add_argument('--gan_future_length', action='store', type=int, default=10, help="")
    parser.add_argument('--mse_coeff', action='store', type=float, default=0.5, help="")
    parser.add_argument('--postop_emr_coeff', action='store', type=float, default=1.0, help="coefficient for postop emr coefficient (in GAN)")
    parser.add_argument('--postop_emr_prediction', action='store', type=bool, default=False, help="train emr or not (in the older model)")
    parser.add_argument('--verbose', action='store_true', default=None, help="")
    parser.add_argument('--fingerprints_filename', action='store', default=None, help="")
    parser.add_argument('--input_surgeon_id', action='store_true', default=None, help="")
    parser.add_argument('--model_analysis_modes', nargs='+', default = ['phase_identification'],
                        help="Define which modes of analysis are available by the model")

    if additional_setters is not None:
        if type(additional_setters) is not list:
            additional_setters = [additional_setters]
        for setter in additional_setters:
            parser = setter(parser)

    args = parser.parse_args()
    return args